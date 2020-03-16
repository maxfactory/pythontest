# n = eval(input("请输入一个数字："))
# if type(n) == type(111):
#     print("输入的数字是整数")
# elif type(n) == type(1.11):
#     print("输入的数字是浮点数")
# else:
#     print("无法判断输入类型")

# all_data = [['John', 'Emily', 'Michael', 'Mary','Steven'],
#             ['Maria', 'Juan', 'Javier', 'Natalia','Pilar']]
# names_of_interest = []
# for names in all_data:
# ##    enough_es = [name for name in names if name.count('e') >= 2]
#     for name in names:
#         if name.count('e') >= 2:
#             names_of_interest.append(name)
# print(names_of_interest)

# name = ['cq','Steven']
# names = []
# for na in name:
# 	if na.count('e') >= 2:

# 		names.extend(na)
# print(names)

# name = ['Steven']
# names = []
# for na in name:
# 	if na.count('e') >= 2:
# 		names.append(na)
# print(names)

import random
for i in range(10):
	a = random.random()
	print(a)