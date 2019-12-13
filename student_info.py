

grade_list = []
str_print = "姓名：{}\t数学成绩：{}\t语文成绩：{}\t英语成绩：{}"
while 1:
	print("""
#####################################################
【学生信息管理系统】
1、新建学生信息
2、显示全部信息
3、查询学生信息
4、删除学生信息
5、修改学生信息

0、退出系统
#####################################################
""")
	action = input("请输入你想要进行的操作：\n")
	if action == '1':
		""" 新建学生信息 """
		name = input("请输入名字：")
		math = input("请输入数学成绩：")
		chinese = input("请输入语言成绩：")
		english = input("请输入英语成绩：")
		total = int(math) + int(chinese) + int(english)
		grade_list.append([name,math,chinese,english,total])
		# print("姓名：{}\t数学成绩：{}\t语文成绩：{}\t英语成绩：{}".format(name,math,chinese,english,total))
		print(str_print.format(name,math,chinese,english,total))
	elif action == '2':
		""" 显示全部信息 """
		for info in grade_list:
			# print(str_print.format(name,math,chinese,english,total))
			# 列表解包
			print(str_print.format(*info))

	elif action == '3':
		""" 查询学生信息 """
		name =  input("请输入你需要查询学生的姓名：")
		for info in grade_list:
			if name in info:
				print(str_print.format(*info))
				break
		# else 与 for 一起使用   for正常结束就运行else
		else:
			print("此学生不存在")

	elif action == '4':
		""" 删除学生信息 """
		name =  input("请输入你需要删除学生的姓名：")
		for info in grade_list:
			if name in info:
				# 弹出
				info_ = grade_list.pop(grade_list.index(info))
				print("这个学员的信息已经被删除\n",info_)
				break
		else:
			print("此学生不存在")
		
	elif action == '5':
		""" 修改学生信息 """
		name =  input("请输入你需要修改学生的姓名：")
		for info in grade_list:
			if name in info:
				# 得到学生信息在列表中的位置
				index = grade_list.index(info)
				break
		else:
			print("此学生不存在")
			continue
		math = input("请输入数学成绩：")
		chinese = input("请输入语言成绩：")
		english = input("请输入英语成绩：")
		total = int(math) + int(chinese) + int(english)
		grade_list[index][1:] = [math,chinese,english,total]
		print("修改后的成绩：", grade_list[index])
		
	elif action == '0':
		""" 退出系统 """
		break
	else:
		print("输入信息有误，请重新输入")