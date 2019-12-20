import json
filename = 'numbers.json'
with open(filename) as f_obj:
	# 如果用这种方法读取文件的话，将会把读取后的文件改变为字符串类型
	# numbers = f_obj.read()

	# 用这种方法，在读取文件后将不会改变其属性
	numbers = json.load(f_obj)
for num in numbers:
	print(num)
a = type(numbers)
print(a)