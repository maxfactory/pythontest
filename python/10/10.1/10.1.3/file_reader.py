filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		# print(line)
		# 消除空白行
		print(line.rstrip())