#!/usr/bin/env python3
TempStr = input("请输入带有符号的温度值：")
if TempStr[-1] in ['F','f']:   #判断一个数的位数是否在一个列表中
	C = (eval(TempStr[:-1]) - 32)/1.8
	print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
	F = 1.8*eval(TempStr[:-1]) + 32
	print("转换后的温度是{:.2f}F".format(F))
else:
	print("输入格式错误")
	