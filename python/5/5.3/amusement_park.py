# age = 12
# if age < 4:
# 	print("Your admission cost is $0.")
# elif age < 18:
# 	print("Your admission cost is $5.")
# else:
# 	print("Your admission cost is $10.")

# 改写
# age = 12
# if age < 4:
# 	price = 0
# elif age < 18:
# 	price = 5
# else:
# 	price = 10

# print("Your admission cost is $" + str(price) + ".")

# 使用多个elif语句
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
else:
	price = 5

print("Your admission cost is $" + str(price) + ".")