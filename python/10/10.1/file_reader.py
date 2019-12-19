with open('pi_digits.txt') as file_object:
	# 使用方法 read() 读取文件全部内容，并将其作为一个长长的字符串存储在变量contents中
	contents = file_object.read()
	# print(contents)

	#使用 rstrip() 可以消除打印出来的字符串末尾的空白。
	print(contents.rstrip())