#!/usr/bin/env python3
from random import random
from time import perf_counter    #time库计时
DARTS = 1000*1000               #初始量，抛洒点的总数量
hits = 0.0                      #目前在圆的内部的点的数量
start = perf_counter()          #启动计时
for i in range(1,DARTS+1):
	x,y = random(),random()
	dist = pow(x**2 + y**2,0.5)  #点到圆心的距离
	if dist <= 1.0:
		hits = hits+1
pi = 4* (hits/DARTS)
print("圆周率值是: {}".format(pi))
print("运行时间是：{:.5f}s".format(perf_counter()-start))

#求解圆周率可以采用蒙特卡罗方法，在一个正方形中撒点，根据在1/4内点的数量占总撒点数比例计算圆周率值。
#请以123作为随机数种子，获得用户输入的撒点数量，编写程序输出圆周率的值，保留小数点后6位。
from random import random, seed
DARTS = eval(input())
seed(123)
hits = 0.0
for i in range(DARTS):
	x, y = random(), random()
	dist = pow(x ** 2 + y ** 2, 0.5)
	if dist <= 1.0:
		hits = hits + 1
pi = 4 * (hits/DARTS)
print("{:.6f}".format(pi))