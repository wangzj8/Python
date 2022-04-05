#!/usr/bin/env python3
#求100以内所有素数之和并输出。 ‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬
#素数指从大于1，且仅能被1和自己整除的整数。‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬
#提示：可以逐一判断100以内每个数是否为素数，然后求和。  模仿天天向上力量的函数

#for i in range(2,100):
#	for j in range(2,i):
#		if(i%j==0):
#			break
#	else:
#		s+=i
#print(s)
#


def is_prime(n):  #n 形参
	
	for i in range(2,n):
		if n%i == 0:
			return False
	return True

# main
if __name__ == "__main__":
	sum = 0
	for i in range(2,100):
		if is_prime(i):
			sum += i
		else: 
			print("not prime")
	print(sum)
	