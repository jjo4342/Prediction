# The `Environments` class represents a simulation environment for multiple agents moving in lanes,
# with functionalities for spawning agents, running simulations, filtering sensor information,
# predicting future positions, and visualizing predicted trajectories.
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

from kalman_filter import KalmanFilter


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
            if id_ == 0:
                # 1) Sensor 정보 수신
                sensor_info = self.vehicles[id_].get_measure(self.vehicles)
                # print("sensor_info : ", sensor_info)

                # 2) 자 차량 정보를 활용하여 global 좌표로 변환
                global_sensor_info = self.transform_sensor_info(self.vehicles[id_], sensor_info)
                # print("global_sensor_info : ", global_sensor_info)

                # 3) 노이즈 필터링
                filtered_sensor_info = self.filter_sensor_info(global_sensor_info)
                # print("filtered_sensor_info : ", filtered_sensor_info, "\n\n")

                # local_lane_info = self.vehicles[id_].get_local_path()

                sdv_current_lane = self.find_current_lane(self.vehicles[id_].x, self.vehicles[id_].y, self.map_pt)

                should_stop = False

                for info in filtered_sensor_info:

                    # 4) Agent별 현재 차선 후보 탐색
                    agent_current_lane = self.find_current_lane(info['x'], info['y'], self.map_pt)
                    # print(info['id'],": Lane", agent_current_lane)

                    # 5) Agent별 의도 예측
                    agent_state = self.predict_agent_intent(info['vx'], info['vy'])
                    # print(info['id'],": Lane", agent_state)

                    # 6) 주변 agent에 따른 SDV 제어
                    if (sdv_current_lane != 4 and
                    (agent_current_lane in self.crossing_info(self.course_idx) or agent_current_lane == sdv_current_lane)):
                        if agent_state == 'Forward':
                            should_stop = True
                            break

                if should_stop:
                        self.vehicles[id_].step_manual(ax=-2, steer=0)  # SDV 정지
                else:
                        self.vehicles[id_].step_manual(ax=1, steer=0)  # SDV 전진


            if id_  > 0 :
                self.vehicles[id_].step_auto(self.vehicles, self.int_pt_list[id_])


    def transform_sensor_info(self, vehicle, sensor_info):
        global_sensor_info = [
            {
                'id': info[0],
                'x': vehicle.x + info[1] * np.cos(vehicle.h) - info[2] * np.sin(vehicle.h),
                'y': vehicle.y + info[1] * np.sin(vehicle.h) + info[2] * np.cos(vehicle.h),
                'h': vehicle.h + np.arctan2(info[2], info[1]),
                'vx': info[4] * np.cos(vehicle.h) - info[5] * np.sin(vehicle.h),
                'vy': info[4] * np.sin(vehicle.h) + info[5] * np.cos(vehicle.h)
            }
            for info in sensor_info
        ]
        return global_sensor_info


    def filter_sensor_info(self, sensor_info):
        filtered_sensor_info = []
        for info in sensor_info:
            z = np.array([info['x'], info['y'], info['vx'], info['vy']]).reshape(-1, 1)
            self.kf.predict()
            self.kf.correction(z)

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


    def find_current_lane(self, x, y, map):
        min_dist = float("inf")
        nearest_lane = None

        for lane, lane_points in map.items():
            for lane_point in lane_points:
                distance = ((x - lane_point[0])**2 + (y - lane_point[1])**2)**0.5
                if distance < min_dist:
                    min_dist = distance
                    nearest_lane = lane
        return nearest_lane


    def find_adjacent_lane(self, current_lane):
        connected_lanes = self.connectivity[current_lane]
        adjacent_lanes = []
        for idx, connected in enumerate(connected_lanes):
            if connected == 1:
                adjacent_lanes.append(idx)
        return adjacent_lanes


    def crossing_info(self, course_idx):
        crossing_lane_info = []
        if course_idx == 0: # 좌회전
            crossing_lane_info = [5, 6, 7, 14, 15, 21, 22]

        elif course_idx == 1: # 직진
            crossing_lane_info = [5, 6, 7, 8, 14, 15 ,16, 22]

        elif course_idx == 2: # 우회전
            crossing_lane_info = [15]

        return crossing_lane_info


    def predict_agent_intent(self, velocity_x, velocity_y):

        if abs(velocity_x) <= 1 and abs(velocity_y) <= 1:
            predict = 'Stop'
        else:
            predict = 'Forward'
        return predict


    def respawn(self):
        if len(self.vehicles)<self.min_num_agent:
            self.spawn_agent()




if __name__ == '__main__':

    try:
        f = Environments()

    except rospy.ROSInterruptException:
        rospy.logerr('Could not start node.')




