#!/usr/bin/env python3
#例题5-2
food = 'Beef'
if food == 'beef':
	print(True)
else:
	print(False)
food = food.lower()
if food == 'beef':
	print(True)
requested_toppings = ['mushrooms','onions','pineapple']
if 'mushrooms' in requested_toppings:
	print(True)
else:
	print(False)
banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
	print(f"{user.title()},you are")