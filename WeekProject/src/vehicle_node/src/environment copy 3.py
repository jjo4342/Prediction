#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pickle
import glob
import copy
import bisect
import matplotlib.cm as cm
import matplotlib.animation as animation

from IPython.display import HTML
from utils import *
from agent import agent


import tf
import rospkg
import rospy

from geometry_msgs.msg import Twist, Point32, PolygonStamped, Polygon, Vector3, Pose, Quaternion, Point
from visualization_msgs.msg import MarkerArray, Marker

from std_msgs.msg import Float32, Float64, Header, ColorRGBA, UInt8, String, Float32MultiArray, Int32MultiArray

from kalman_filter_sub import KalmanFilter  # kalman_filter_sub.py에서 KalmanFilter 클래스 임포트


class Environments(object):
    def __init__(self, course_idx, dt=0.1, min_num_agent=8):
                
        self.spawn_id = 0
        self.vehicles = {}
        self.int_pt_list = {}
        self.min_num_agent = min_num_agent
        self.dt = dt
        self.course_idx = course_idx

        # Kalman Filter 초기화
        # x_dim과 z_dim은 예시로 4로 설정 (상황에 맞게 조정 필요)
        self.kf = KalmanFilter(x_dim=4, z_dim=4)
        self.kf.A = np.eye(4)  # 상태 전이 행렬 설정
        self.kf.H = np.eye(4)  # 관측 행렬 설정
        self.kf.Q = 0.01 * np.eye(4)  # 프로세스 노이즈 공분산
        self.kf.R = 0.01 * np.eye(4)  # 측정 노이즈 공분산

        self.initialize()

    def initialize(self, init_num=6):
        
        self.pause = False
        filepath = rospy.get_param("file_path")
        Filelist = glob.glob(filepath+"/*info.pickle")
        
        file = Filelist[0]

        with open(file, "rb") as f:
            Data = pickle.load(f)
            
        self.map_pt = Data["Map"]
        self.connectivity = Data["AS"]
        
        for i in range(init_num):
            if i==0:
                ## 타겟 차선 정보 (좌/직/우)
                CourseList = [[4,1,18], [4,2,25], [4,0,11]]
                self.spawn_agent(target_path = CourseList[self.course_idx], init_v = 0)
            else:
                self.spawn_agent()
         
    
    def spawn_agent(self, target_path=[], init_v = None):
        
        is_occupied = True
        
        if target_path:
                      
            spawn_cand_lane = target_path[0]
            is_occupied = False
            s_st = 5
            
        else:
            spawn_cand_lane = [10,12,24,17,19]

            s_st = np.random.randint(0,20)
            max_cnt = 10
            while(is_occupied and max_cnt>0):
                
                spawn_lane = np.random.choice(spawn_cand_lane)
                
                is_occupied = False
                for id_ in self.vehicles.keys():
                    if (self.vehicles[id_].lane_st == spawn_lane) and np.abs(self.vehicles[id_].s - s_st) < 25:
                        is_occupied = True    
                        
                max_cnt-=1            
        
        if is_occupied is False:
            if target_path:
                target_path = target_path
                
            else:
                target_path = [spawn_lane]
                spawn_lane_cand = np.where(self.connectivity[spawn_lane]==1)[0]
                
                while(len(spawn_lane_cand)>0):
                    spawn_lane = np.random.choice(spawn_lane_cand)
                    target_path.append(spawn_lane)
                    spawn_lane_cand = np.where(self.connectivity[spawn_lane]==1)[0]
            
            target_pt = np.concatenate([self.map_pt[lane_id][:-1,:] for lane_id in target_path], axis=0)
            self.int_pt_list[self.spawn_id] = {}
            
            for key in self.vehicles.keys():
                intersections = find_intersections(target_pt[:,:3], self.vehicles[key].target_pt[:,:3]) # ((x,y), i, j)
                
                if intersections:
                    self.int_pt_list[self.spawn_id][key] = [(inter, xy[0], xy[1]) for (inter, xy) in intersections]
                    self.int_pt_list[key][self.spawn_id] = [(inter, xy[1], xy[0]) for (inter, xy) in intersections]
                                
            stopline_idx = len(self.map_pt[target_path[0]])-1
            endline_idx = len(self.map_pt[target_path[0]])+len(self.map_pt[target_path[1]])-2
                
            self.vehicles[self.spawn_id] = agent(self.spawn_id, target_path, s_st, target_pt, dt=self.dt, init_v = init_v,
                                                 stoplineidx = stopline_idx, endlineidx = endline_idx)
            self.spawn_id +=1
    
    def delete_agent(self):
        
        delete_agent_list = []
        
        for id_ in self.vehicles.keys():
            if (self.vehicles[id_].target_s[-1]-10) < self.vehicles[id_].s:
                delete_agent_list.append(id_)
            
        return delete_agent_list
                    
    def run(self):
        
        for id_ in self.vehicles.keys():
            vehicle = self.vehicles[id_]  # 각 차량 객체에 접근

            # 1) Sensor 정보 수신
            sensor_info = vehicle.get_measure(self.vehicles)
            # print("1. ", sensor_info, "\n")

            # 2) 자 차량 정보를 활용하여 global 좌표로 변환
            global_sensor_info = self.transform_sensor_info_to_global(vehicle, sensor_info)
            # print("2. ", global_sensor_info, "\n")

            # 3) 노이즈 필터링 및 필터링된 데이터 저장
            filtered_sensor_info = self.filter_sensor_info(vehicle, global_sensor_info)
            # print("3. ", filtered_sensor_info, "\n")

            # 4) Agent별 현재 차선 후보 탐색 및 5) Agent별 갈 수 있는 차선 후보 탐색
            current_lane = vehicle.lane_st
            possible_lanes = [lane for lane in range(len(self.map_pt)) if self.connectivity[current_lane][lane]]
            # print(id_,":",current_lane, "-> " ,possible_lanes,"\n")

            # 6) Agent별 경로 혹은 의도 예측
            predicted_paths = {}
            for info in filtered_sensor_info:
                predicted_paths[info['id']] = self.predict_path(vehicle, info, possible_lanes)
            # print(predicted_paths)

            # 7) 주변 agent에 따른 SDV 종 / 횡 방향 제어
            if id_ == 0:  # SDV의 경우 특별한 로직 처리
                conflict_detected = False
                for info in filtered_sensor_info:
                    if self.is_conflict(vehicle, info, predicted_paths[info['id']]):
                        vehicle.step_manual(ax=0, steer=0)  # 긴급 정지
                        conflict_detected = True
                        print("Emergency stop due to predicted collision at intersection.")
                        break
                if not conflict_detected:
                    vehicle.step_manual(ax=0.4, steer=0)  # 정상 주행

            if id_  > 0 :
                self.vehicles[id_].step_auto(self.vehicles, self.int_pt_list[id_])



    def transform_sensor_info_to_global(self, vehicle, sensor_info):
        global_sensor_info = [
            {
                'id': info[0],
                'x': vehicle.x + info[1] * np.cos(vehicle.h) - info[2] * np.sin(vehicle.h),
                'y': vehicle.y + info[1] * np.sin(vehicle.h) + info[2] * np.cos(vehicle.h),
                'h': vehicle.h + np.arctan2(info[2], info[1]),
                'vx': info[4],
                'vy': info[5]
            }
            for info in sensor_info
        ]
        return global_sensor_info


    def filter_sensor_info(self, vehicle, sensor_info):
        filtered_sensor_info = []
        for info in sensor_info:
            z = np.array([info['x'], info['y'], info['vx'], info['vy']]).reshape(-1, 1)  # 측정 벡터
            self.kf.predict()  # 상태 예측
            self.kf.correction(z)  # 상태 업데이트

            # 필터링된 상태를 filtered_sensor_info에 추가
            filtered_info = {
                'id': info['id'],
                'x': self.kf.x_post[0, 0],
                'y': self.kf.x_post[1, 0],
                'h': info['h'],
                'vx': self.kf.x_post[2, 0],
                'vy': self.kf.x_post[3, 0]
            }
            filtered_sensor_info.append(filtered_info)
        return filtered_sensor_info


    def ctra_predict(self, x, y, theta, v, omega, a, dt):
        """
        CTRA 모델을 사용하여 차량의 미래 위치를 예측합니다.
        """
        if omega == 0:  # 회전율이 0인 경우, 일반적인 직선 운동
            x_new = x + v * np.cos(theta) * dt
            y_new = y + v * np.sin(theta) * dt
        else:  # 회전 운동이 있는 경우
            x_new = x + (v/omega) * (np.sin(theta + omega*dt) - np.sin(theta))
            y_new = y + (v/omega) * (-np.cos(theta + omega*dt) + np.cos(theta))
        
        theta_new = theta + omega * dt
        v_new = v + a * dt
        
        return x_new, y_new, theta_new, v_new

    def predict_path(self, vehicle, sensor_info, possible_lanes):
        """
        차량의 경로를 CTRA 모델을 사용하여 예측합니다.
        """
        dt = 2  # 1초 후의 위치를 예측
        x_new, y_new, _, _ = self.ctra_predict(
            x=vehicle.x,
            y=vehicle.y,
            theta=vehicle.h,
            v=sensor_info['vx'],  # 속도 정보
            omega=np.random.uniform(-0.1, 0.1),  # 회전율: 랜덤값 예제
            a=0,  # 가속도: 0으로 가정
            dt=dt
        )
        
        # 예측된 위치를 기반으로 다음 차선 결정
        lane_distances = {lane: np.linalg.norm(np.array([x_new, y_new]) - self.map_pt[lane][-1][:2]) for lane in possible_lanes}
        next_lane = min(lane_distances, key=lane_distances.get)
        return next_lane

    def is_conflict(self, vehicle, sensor_info, predicted_path):
        # 충돌 검사 로직 (간단한 예시)
        predicted_pos_x = sensor_info['x'] + sensor_info['vx'] * 2  # 2초 후 예상 위치
        predicted_pos_y = sensor_info['y'] + sensor_info['vy'] * 2
        if abs(predicted_pos_x - vehicle.x) < 1 and abs(predicted_pos_y - vehicle.y) < 1:
            return True
        return False



    def respawn(self):
        if len(self.vehicles)<self.min_num_agent:
            self.spawn_agent()
                    
if __name__ == '__main__':

    try:
        f = Environments()

    except rospy.ROSInterruptException:
        rospy.logerr('Could not start node.')




