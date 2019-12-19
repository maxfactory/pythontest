filename = 'pi_million_digits1.txt'
with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	# pi_string += line.rstrip()
	pi_string += line.strip()

# 判断生日是否包含于pi中
birthday = input("Enter your birthday,in the form mmddyy: ")
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi!")
else:
	print("Your birthday does not appears in the first million digits of pi!")


# 打印小数点后50位的pi，并打印总长度
# print(pi_string[:52] + "...")
# print(len(pi_string))