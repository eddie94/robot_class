from math import *
import random

landmarks=[[0,0],[0,100],[100,0],[100,100]]
landmark_name=['landmark 1','landmark 2','landmark 3','landmark 4']
world_size=100
max_steering_angle=pi/4

class robot():

    def __init__(self):
        self.x=random.random()*world_size
        self.y=random.random()*world_size
        self.orientation=random.random()*2*pi
        self.forward_noise=0
        self.turn_noise=0
        self.sense_noise=0

    def __repr__(self):
        return('[x=%.6s y=%.6s orient=%.6s]' % (str(self.x),str(self.y),str(self.orientation)))

    def set(self,new_x,new_y,new_orient):

        if new_orient<0 or new_orient>=2*pi:
            raise(ValueError, 'orientation must be between 0~2pi')
        if new_x<0 or new_x>=world_size:
            raise (ValueError, 'x is out of bound')
        if new_y<0 or new_y>=world_size:
            raise (ValueError, 'y is out of bound')

        self.x=float(new_x)
        self.y=float(new_y)
        self.orientation=float(new_orient)

    def set_noise(self,new_f_noise,new_t_noise,new_s_noise):
        self.forward_noise=float(new_f_noise)
        self.turn_noise=float(new_t_noise)
        self.sense_noise=float(new_s_noise)

    def move(self,turn,forward):

        x=0
        y=0

        if forward<0:
            raise (ValueError, 'robot cannot move backwards')

        if turn > max_steering_angle:
            turn = max_steering_angle

        orientation = self.orientation + float(turn) + random.gauss(0.0,self.turn_noise)
        orientation %= 2*pi

        dist = float(forward) + random.gauss(0.0,self.forward_noise)
        x = self.x + (cos(orientation) * dist)
        y = self.y + (sin(orientation) * dist)

        if x > world_size:
            x = world_size
        if y > world_size:
            y = world_size

        self.x = x
        self.y = y

    def sense(self):
        d=[]
        for i in range(len(landmarks)):
            distance_x=self.x-landmarks[i][0]
            distance_y=self.y-landmarks[i][1]
            value=abs(sqrt(pow(distance_x,2)+pow(distance_y,2)))
            d.append(value)

        for i in range(len(landmarks)):
            print('distance from %s is %.6s' %(landmark_name[i], d[i]))

