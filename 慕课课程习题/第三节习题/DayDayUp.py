#!/usr/bin/env python3
dayup = 1.0  #进步 1%
dayfactor = 0.01   #退步千分之一
for i in range(365):
	if i % 7 in [6,0]:   #工作五天，休息两天
		dayup = dayup*(1-dayfactor)   #休息日
	else:
		dayup = dayup*(1+dayfactor)   #工作日
dayup1 =round(dayup,2)
print(f"工作日的力量:{dayup1}")