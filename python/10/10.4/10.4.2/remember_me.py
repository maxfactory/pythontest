import json

username = input("What is your name? ")

filename = 'username.json'
with open(filename,'w',encoding='utf-8') as f_obj:
	json.dump(username,f_obj)
	msg = "We'll remember you when you come back," + username.title() + "!"
	print(msg)