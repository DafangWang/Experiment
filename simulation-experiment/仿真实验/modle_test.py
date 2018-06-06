# -*- coding: utf-8 -*-
'''
@author: 程哲
@contact: 909991719@qq.com
@file: modle_test.py
@time: 2017/11/2 11:14
'''
import gym
import time
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt

env=gym.make('Acrobot-v1')
# env=gym.make('Pendulum-v0')
# env=gym.make('Pendulum-v0')
env.reset()
env=env.unwrapped
theta1=[]
theta2=[]
dtheta1=[]
dtheta2=[]

for step in range(env.spec.timestep_limit):
    image=env.render(mode='rgb_array')

    print(np.shape(image))
    time.sleep(0.1)
    action=[0]
    ob,r,done,inf=env.step(action)
    if done:
        time.sleep(10)
        break
    matplotlib.image.imsave(r'figure\name.png', image)
    # theta1.append(inf[1][0])
    # theta2.append(inf[1][1])
    # dtheta1.append(inf[1][2])
    # dtheta2.append(inf[1][3])
    # print(inf[0])
    # ob,r,done,inf=env.step([0])
    # print(inf)
# plt.figure('响应曲线')
# plt.plot(theta1,label='theta1')
# plt.plot(theta2,label='theta2')
# plt.legend()
# plt.figure('角速度')
# plt.plot(dtheta1)
# plt.plot(dtheta2)
# plt.show()