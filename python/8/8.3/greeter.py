# 以更正规的方式问候用户
def get_fomatted_name(first_name,last_name):
	"""返回整洁的名字"""
	full_name = first_name + ' ' + last_name
	return full_name.title()

# 这是一个无限循环
while True:
	print("\nPlease tell me your name? ")
	f_name = input("First name: ")
	if f_name == 'quit':
		break
	l_name = input("Last name: ")
	if l_name == 'quit':
		break
	formatted_name = get_fomatted_name(f_name,l_name)
	print("\nHello " + formatted_name + "!")