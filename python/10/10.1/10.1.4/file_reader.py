# 在with 代码块中将文件 pi_digits.txt 的各行存储在一个列表中，再在with 代码块外打印它们
filename = 'pi_digits.txt'

with open(filename) as file_object:
	# 方法 readlines() 从文件中读取每行，并将其存储在一个列表中
	lines = file_object.readlines()
	print(lines)

for line in lines:
	print(line.rstrip())