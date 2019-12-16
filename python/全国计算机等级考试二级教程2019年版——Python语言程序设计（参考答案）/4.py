# 4.获得用户输入的一个小数，提取并输出其整数部分。
a = input("请输入：")
i = 0
while i < len(a):
	if a[i] == '.':
		print(a[0:i+1])
		break
	i += 1
if i == len(a):
	print(a)