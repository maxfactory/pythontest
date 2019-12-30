import json
#如果以前存储了用户名，就加载它
#否则，就提示用户输入用户名并存储它
filename = 'username.json'
try:
	with open(filename) as f_obj:
		username = json.load(f_obj)
except FileNotFoundError:
	username = input("Please tell me your name:")
	with open(filename,'w') as f_obj:
		json.dump(username,f_obj)
else:
	print("Welcome back," + username.title() + "!")

#-----------------------------------------------------
# filename = 'username.json'
# username = input("Please tell me your name:")
# un = []
# try:
# 	with open(filename,encoding='utf-8') as f_obj:
# 		uname = json.load(f_obj)
# except FileNotFoundError:
# 	with open(filename,'w',encoding='utf-8') as f_obj:
# 		json.dump(username + "\n",f_obj)
# else:
# 	if username in uname:
# 		print("Welcome back," + username.title() + "!")
# 	else:
# 		with open(filename,'a',encoding='utf-8') as f_obj:
# 			json.dump(username + "\n",f_obj)