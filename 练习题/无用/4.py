#!/usr/bin/env python3
#输入三个整数x,y,z，请把这三个数由小到大输出。
numbers = []
for i in range(3):
	x = int(input('intrger:\n'))
	numbers.append(x)
numbers.sort()
print(numbers)
