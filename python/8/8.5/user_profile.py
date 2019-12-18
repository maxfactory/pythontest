# 使用任意数量的关键字实参
# 形参 **user_info 中的两个星号让Python创建一个名为 user_info 的空字典
def build_profile(first,last,**user_info):
	"""创建一个字典，其中包含我们知道的有关用户的一切"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key,value in user_info.items():
		profile[key] = value
	return profile
user_profile = build_profile('albert','einstein',location='princeton',field='physics',sex='men',age=13)
print(user_profile)