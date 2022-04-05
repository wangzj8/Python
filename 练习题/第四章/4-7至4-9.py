#!/usr/bin/env python3
#例题4-7
#numbers=list(range(3,31,3))
#print(numbers)
#for number in numbers:
#	print(number)
#例题4-8
#numbers=[]
#for value in range(1,11):
#	number=value**3
#	numbers.append(number)
#print(numbers)
#例题4-9
numbers=[value**3 for value in range(1,11)]
print(numbers)