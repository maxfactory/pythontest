# 使用文件的内容
# 将创建一个字符串，它包含文件中存储的所有数字，且没有任何空格
filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	# pi_string += line.rstrip()
	pi_string += line.strip()
print(pi_string)
print(len(pi_string))