#!/usr/bin/env python3
def dayUp(df):      #定义函数
	dayup = 1
	for i in range(365):
		if i % 7 in [6,0]:
			dayup = dayup*(1-0.01)
		else:
			dayup = dayup*(1+df)
	return dayup
df = 0.01
while dayUp(df) < 37.78:
	df += 0.001
print("工作日的努力参数是:{:.3f}".format(df))