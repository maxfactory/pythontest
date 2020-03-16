###读取用户输入的数值，并计算平均值
# print("方法一：")
# numbers = []
# while True:
# 	num = input("请输入数字：")
# 	try:
# 		numbers.append(float(num))
# 	except:
# 		print("不是合法的输入！")
# 	while True:
# 		flag = input("需要继续输入吗？(yes/no)")
# 		if flag.lower() not in ('yes','no'):
# 			print("只能输入yes或者no")
# 		else:
# 			break
# 	if flag.lower() == 'no':
# 		break

# print(sum(numbers)/len(numbers))

print("##"*20)

print("方法二：")
numbers = []
while True:
	x = eval(input("请输入数字："))
	numbers.append(x)
	flag = input("是否继续输入：(yes/no)")
	if flag.lower() == 'yes':
		continue
	else:
		print(sum(numbers)/len(numbers))