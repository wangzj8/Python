#!/usr/bin/env python3
#例题5-9
#usernames = ['admin','jaden','jack','mary','david']
#for username in usernames:
#	if username == 'admin':
#		print(f"Hello {username},would you like to see a status report")
#	else:
#		print(f"Hello {username},thank you")
#例题5-9
#usernames = []
#if usernames:
#	for username in usernames:
#		print(username.title())
#else:
#		print("We need to find some users")
#例题5-10
current_users = ['admin','jaden','jack','mary','david']
new_users = ['Join','sonid','men','MARY','david']
#for new_user in new_users:
#	if new_user in current_users:
#		print("need put another")
#	else:
#		print("this name ok")
lower_current_users = [] 
for current_user in current_users:
	lower_current_users.append(current_user.lower())
for new_user in new_users:
	if new_user.lower() in lower_current_users:
		print("need put another")
	else:
		print("this n me ok")
		
#例题5-11
#numbers = ['1','2','3','4','5','6','7','8','9']
#for number in numbers:
	#if number == str(1):
	#	print(number+'st')
	#elif number == str(2):
#		print(number+'nd')
#	elif number == str(3):
#		print(number+'rd')
#	else:
#		print(number+'th')	