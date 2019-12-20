import json
filename = 'username.json'
with open(filename) as f_obj:
	name = json.load(f_obj)
	print(name)