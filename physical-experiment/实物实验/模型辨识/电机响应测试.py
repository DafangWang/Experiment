# -*- coding: utf-8 -*-
'''
@author: 程哲
@contact: 909991719@qq.com
@time: 2018/3/29 15:34
'''

import time
import numpy as np
import matplotlib.pyplot as plt


from PyDAQmx import *
from sensor import *


if __name__=='__main__':

    sen = CONTROL()
    sen.start()

    Theta2=[]
    T_get=[]
    T_send=[]
    Time=[]
    start_time=time.clock()
    for step in range(200):
        #方波
        if step<50:
            value=0
        elif 50<=step and step<100:
            value=0.5
        else:
            value=-0.5
        #正弦波
        # if step<50:
        #     value=0
        # else:
        #     value=0.5*np.sin(0.05*(step-49))

        angle1, angle_velocity1 = sen.read_ahrs()
        angle2, angle_velocity2, torque = sen.read_daq()
        sen.write_daq(10/2.73*value)
        Time.append(time.clock()-start_time)
        T_send.append(10*value)
        T_get.append(torque)
    sen.stop()
    print(time.clock()-start_time)
    plt.figure('动作')
    plt.plot(Time,T_send,label="Torque_send")
    plt.plot(Time,T_get, label="Torque_get")
    plt.legend()
    plt.show()








