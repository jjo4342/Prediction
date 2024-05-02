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
        
        self.agent_crossing_lanes = {}

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

            self.update_sdv_crossing_lanes()
            self.update_agent_crossing_lanes()

            # 1) Sensor 정보 수신
            sensor_info = vehicle.get_measure(self.vehicles)

            # 2) 자 차량 정보를 활용하여 global 좌표로 변환
            global_sensor_info = self.transform_sensor_info_to_global(vehicle, sensor_info)

            # 3) 노이즈 필터링 및 필터링된 데이터 저장
            filtered_sensor_info = self.filter_sensor_info(vehicle, global_sensor_info)

            # 4) Agent별 현재 차선 후보 탐색 및 5) Agent별 갈 수 있는 차선 후보 탐색
            current_lane = vehicle.lane_st
            possible_lanes = [lane for lane in range(len(self.map_pt)) if self.connectivity[current_lane][lane]]

            # 7) 주변 agent에 따른 SDV 종 / 횡 방향 제어
            if id_ == 0:  # SDV의 경우 특별한 로직 처리
                
                for info in filtered_sensor_info:
                    if self.is_conflict(vehicle, info):
                        vehicle.step_manual(ax=-20, steer=0)  # 긴급 정지
                    else:
                        vehicle.step_manual(ax=0.1, steer=0)  # 정상 주행


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


    def is_conflict(self, vehicle, sensor_info):
        agent_id = sensor_info['id']

        intersections = self.int_pt_list.get(agent_id, {})

        for other_id, crossing_points in intersections.items():
            if other_id == 0:
                continue  # 자기 자신과의 교차점은 무시

            other_vehicle = self.vehicles.get(other_id)
            if not other_vehicle:  # 다른 에이전트가 존재하지 않으면 무시
                continue

            for inter, pos_self, pos_other in crossing_points:
                # 교차점과 SDV의 거리 계산
                distance_to_intersection_sdv = np.linalg.norm(np.array(inter) - np.array([vehicle.x, vehicle.y]))
                # 교차점과 다른 에이전트의 거리 계산
                distance_to_intersection_other = np.linalg.norm(np.array(inter) - np.array([other_vehicle.x, other_vehicle.y]))
                if other_vehicle.v < 2.5:
                    continue

                if distance_to_intersection_sdv < 5: 
                    if abs(distance_to_intersection_sdv - distance_to_intersection_other) < 5:  # 거리 차이 임계값은 상황에 따라 조절
                        print(f"between vehicle 0 and vehicle {agent_id} \n")
                        return True

        return False




    def update_sdv_crossing_lanes(self):
        if 0 in self.vehicles:
            sdv_lane = self.vehicles[0].lane_st
            self.sdv_crossing_lanes = [lane for lane in range(len(self.map_pt)) if self.connectivity[sdv_lane][lane]]
            # print(f"SDV is in lane {sdv_lane}. Possible crossing lanes: {self.sdv_crossing_lanes}")
        else:
            self.sdv_crossing_lanes = []
            # print("SDV not found. No crossing lanes updated.")



    def update_agent_crossing_lanes(self):
        """각 에이전트의 가능한 교차 차선을 업데이트합니다."""
        for id_, vehicle in self.vehicles.items():
            current_lane = vehicle.lane_st
            self.agent_crossing_lanes[id_] = [lane for lane in range(len(self.map_pt))
                                              if self.connectivity[current_lane][lane]]



    def respawn(self):
        if len(self.vehicles)<self.min_num_agent:
            self.spawn_agent()
                    
if __name__ == '__main__':

    try:
        f = Environments()

    except rospy.ROSInterruptException:
        rospy.logerr('Could not start node.')




