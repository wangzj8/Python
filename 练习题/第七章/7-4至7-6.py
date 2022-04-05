#!/usr/bin/env python3
#pizza = "please write one food: "
#pizza += "\nEnter 'quit' will be end "
#food = ""
#while food != 'quit':
#	food = input(pizza)
#	print(f"i like this {food}")
#movie = "\nHow old are you: "
#price = ""
#while price != 'quit':
#	price = input(movie)
#	price = int(price)
#	if price < 3:
#		print("free")
#	elif price <12:
#		print("ten yaun")
#	else:
#		print("15 yuan")

#第一种方法	
#pizza = "please write one food: "
#pizza += "\nEnter 'quit' will be end "
#food = ""
#while food != 'quit':
#	food = input(pizza)
#	if food != 'quit':		
# 		print(f"i like this {food}")
		
#第二种方法
pizza = "please write one food: "
pizza += "\nEnter 'quit' will be end "
active = True
while active:
	message = input(pizza)
	if message == 'quit':
		active = False
	else:
		print(message)
		
#第三种方法
pizza = "please write one food: "
pizza += "\nEnter 'quit' will be end "
while True:
	message = input(pizza)
	if message == 'quit':
			break
	else:
		print(message)		

			