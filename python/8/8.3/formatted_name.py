# 调用返回值的函数时，需要提供一个变量，用于存储返回的值。在这里，交返回值存储在了变量musician中
# def get_formatted_name(first_name,middle_name,last_name):
# 	"""返回整洁的名字"""
# 	full_name = first_name + ' ' + middle_name + ' ' + last_name
# 	return full_name.title()

# musician = get_formatted_name('jimi','lee','hendrix')
# print(musician)
#--------------------------------------------------
# 将实参变为可选的
def get_formatted_name(first_name,last_name,middle_name=''):
	"""返回整洁的名字"""

	# 判断如果middle_name不为空的话，即为True
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi','hendrix','lee')
print(musician)
musician = get_formatted_name('jimi','hendrix')
print(musician)