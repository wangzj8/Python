#!/usr/bin/env python3

# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
numbers = []
for i in range(1, 5):
	for j in range(1, 5):
		for k in range(1, 5):
			if (i != j) and (j != k) and (i != k):
				numbers.append(i * 100 + j * 10 + k)
print(len(numbers))
print(numbers)

# 有五个数字：0、1、2、3、4，能组成多少个互不相同且无重复数字的两位数？各是多少？
numbers = []
for i in range (0, 5):
	for j in range(0, 5):
		if i == 0:
			continue
		if (i != j):
			numbers.append(i * 10 + j)
print(len(numbers))
print(numbers)
