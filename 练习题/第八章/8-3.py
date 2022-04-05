#!/usr/bin/env python3
#例题8-3
#def make_shirt(shirt_size,shirt_logo):
#	print(f"Shirt size is {shirt_size.title()} and logo is {shirt_logo.title()}")
#make_shirt('L','wgh傻子')

#def make_shirt(shirt_size,shirt_logo):
#	print(f"Shirt size is {shirt_size.title()} and logo is {shirt_logo.title()}")
#make_shirt(shirt_size = 'L',shirt_logo = 'wgh傻子')

#例题8-4
#def make_shirt(shirt_size,shirt_logo = 'I love WGH'):
#	print(f"Shirt size is {shirt_size.title()} and logo is {shirt_logo.title()}")
#make_shirt(shirt_size = 'L')
#make_shirt(shirt_size = 'M')
#make_shirt(shirt_size = 'L',shirt_logo = 'I love python')

#例题8-5
def describe_city(city_name,country_name = 'China'):
	print(f"{city_name} is in {country_name}")
describe_city('shanghai')
describe_city('beijing')
describe_city('dongjing',country_name = 'Janpan')