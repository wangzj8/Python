#!/usr/bin/env python3
#例题4-10
#animinal=['chicken','beef','sheep','dack','fish']
#print(f"The first three items in the list are")
#print(animinal[0:3])
#print(f"\nThree items from the middle of the are")
#print(animinal[1:4])
#print(f"\nThe last three items in the list are")
#print(animinal[2:])
#例题4-11
my_pizzas = ['chicken', 'beef','pork']
friend_pizzas = my_pizzas[:]
print(my_pizzas)
print(friend_pizzas)
my_pizzas.append('fish')
friend_pizzas.append("dack")
print(f"\nMy favorite pizzas are")
for my_pizza in my_pizzas:
	print(my_pizza,)
print(f"\nMy friend's favorite pizzas are")	
for friend_pizza in friend_pizzas:
	print(friend_pizza)
		
	
		