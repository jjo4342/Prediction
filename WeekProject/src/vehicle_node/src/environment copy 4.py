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
        
        self.predicted_paths = {}  # 예측 경로 저장을 위한 딕셔너리

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
        self.update_vehicles_with_predicted_paths()

        for id_ in self.vehicles.keys():
            
            if id_ == 0:  # SDV의 경우
                sensor_info = self.vehicles[id_].get_measure(self.vehicles)
                
                global_sensor_info = self.transform_sensor_info_to_global(self.vehicles[id_], sensor_info)

                filtered_sensor_info = self.filter_sensor_info(self.vehicles[id_], global_sensor_info)
                
                local_lane_info = self.vehicles[id_].get_local_path()
                
                # 교차점과 충돌 가능성 검사
                collision_risk, risk_level = self.evaluate_collision_risk(filtered_sensor_info, local_lane_info)
                
                if collision_risk:
                    if risk_level == 'high':
                        # 충돌 위험이 높은 경우, 차량을 정지
                        self.vehicles[id_].step_manual(ax=0, steer=0)
                        print("Emergency stop to avoid collision.")
                    elif risk_level == 'moderate':
                        # 충돌 위험이 중간 정도인 경우, 속도를 줄임
                        self.vehicles[id_].step_manual(ax=-0.1, steer=0)
                        print("Slowing down due to potential collision risk.")
                else:
                    # 충돌 위험이 없는 경우, 정상 주행
                    self.vehicles[id_].step_manual(ax=0.3, steer=0)
            
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


    def calculate_predicted_path(self, position_x, position_y, vehicle):
        # 차량의 현재 위치와 속도를 기반으로 예측 경로 계산
        # 가정: agent 클래스에는 position과 velocity라는 속성이 있고 접근 가능해야 함
        position_x = vehicle.x
        position_y = vehicle.y
        velocity = vehicle.v

        predicted_path = []
        for step in range(5):  # 다음 5개의 위치를 예측
            next_position = [position_x + velocity * step, position_y + velocity * step]
            predicted_path.append(next_position)
        return predicted_path


    def update_vehicles_with_predicted_paths(self):
        for vehicle_id, vehicle in self.vehicles.items():
            position_x = vehicle.x  # 위치 접근 방식은 vehicle 클래스 구조에 따라 달라질 수 있습니다.
            position_y = vehicle.y  # 위치 접근 방식은 vehicle 클래스 구조에 따라 달라질 수 있습니다.
            velocity = vehicle.v  # 속도 접근 방식은 vehicle 클래스 구조에 따라 달라질 수 있습니다.
            self.predicted_paths[vehicle_id] = self.calculate_predicted_path(position_x, position_y, velocity)


    def process_sensor_info(self, sensor_info):
        for other_vehicle in sensor_info:
            # 여기서 other_vehicle은 사전 형태가 아닐 수 있습니다. 적절히 변환 필요
            if isinstance(other_vehicle, dict) and 'predicted_path' in other_vehicle:
                # 예측 경로와의 교차 검사
                pass
            else:
                # other_vehicle 구조 변환 또는 예외 처리
                print("Invalid vehicle data format")


    def evaluate_collision_risk(self, local_lane_info):
        # 충돌 위험을 평가하고 위험 수준을 반환합니다.
        for vehicle_id, predicted_path in self.predicted_paths.items():
            if self.paths_intersect(local_lane_info, predicted_path):
                # 교차 검사 로직으로 충돌 가능성 평가
                distance = self.calculate_distance(local_lane_info, predicted_path)
                if distance < 2:  # 충돌 위험이 높음
                    return True, 'high'
                elif distance < 5:  # 충돌 위험이 보통
                    return True, 'moderate'
        return False, 'none'  # 충돌 위험이 없음


    def paths_intersect(self, path1, path2):
        # 예제: 두 선분의 교차 여부 확인
        # 두 선분 (path1[0] -> path1[1], path2[0] -> path2[1])
        # 간단한 예시로 각 경로의 첫 번째 두 점만을 사용하여 교차를 계산
        def ccw(A, B, C):
            return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

        def intersect(A, B, C, D):
            # 두 선분 AB와 CD가 교차하는지 확인
            return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

        A, B = path1[0], path1[1]
        C, D = path2[0], path2[1]
        return intersect(A, B, C, D)

    def calculate_distance(self, path1, path2):
        # 두 경로 간의 최소 거리 계산
        # 간단한 예로, 각 경로의 첫 점 사이의 유클리드 거리 사용
        dist = np.linalg.norm(np.array(path1[0]) - np.array(path2[0]))
        return dist


    def respawn(self):
        if len(self.vehicles)<self.min_num_agent:
            self.spawn_agent()
                    
if __name__ == '__main__':

    try:
        f = Environments()

    except rospy.ROSInterruptException:
        rospy.logerr('Could not start node.')




