#!/usr/bin/env python3
#一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
#for i in range (1,85):
#	if 168 % i == 0:
#		j = 168 / i;
#		if 	i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0 :
#			m = (i + j) / 2
#			n = (i - j) / 2
#			x = n * n - 100
#			print(x)

#输出2-100之间的素数
i = 2
while i < 100:
	j = 2
	while j <= i/j:
		if not (i%j):
			break
		j = j+1
	if (j > i/j):
		print(i,"是素数")
	i = i+1
print("Good bye!")