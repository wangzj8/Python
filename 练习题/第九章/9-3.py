#!/usr/bin/env python3
#例题9-1
class Restaurant:
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
	def open_restaurant(self):
		print(f"The {self.restaurant_name} is opening")
		
	def describe_restaurant(self):
		print(f"The {self.restaurant_name} is ")		
		
		
		
this_restaurant = Restaurant('alice', 'relax')
print(f"this restaurant's name is {this_restaurant.restaurant_name}")
print(f"this restaurant's type is {this_restaurant.cuisine_type}")
this_restaurant.open_restaurant()
this_restaurant.describe_restaurant()