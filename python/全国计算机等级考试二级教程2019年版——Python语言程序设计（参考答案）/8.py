# 3.程序读入一个表示星期几的数字（1-7），输出对应的星期字符串名称。例如，输入3，返回“星期三”

# while True:
# 	a = input("请输入一个数字：")
# 	if a == '1':
# 		print("星期一")
# 	elif a == '2':
# 		print("星期二")
# 	elif a == '3':
# 		print("星期三")
# 	elif a == '4':
# 		print("星期四")
# 	elif a == '5':
# 		print("星期五")
# 	elif a == '6':
# 		print("星期六")
# 	elif a == '7':
# 		print("星期日")
# 	else:
# 		break

days = ['星期日','星期一','星期二','星期三','星期四','星期五','星期六',]
num = eval(input("请输入一个数字："))
a = num % 7
print(days[a])