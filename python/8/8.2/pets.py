# 函数后面有两个位置实参
# def describe_pet(animal_type, pet_name):
# 	"""显示宠物的信息"""
# 	print("\nI have a " + animal_type + ".")
# 	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# # 位置实参，函数调用时位置很重要
# describe_pet('hamster','harry')
# describe_pet('dog','willie')

#--------------------------------------
# 关键字实参
# def describe_pet(animal_type, pet_name):
# 	"""显示宠物的信息"""
# 	print("\nI have a " + animal_type + ".")
# 	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet(animal_type='hamster',pet_name='harry')
# describe_pet(pet_name='willie',animal_type='dog')
#----------------------------------------
# 默认值
def describe_pet(pet_name, animal_type='dog'):
	"""显示宠物的信息"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')
describe_pet('harry','hamster')
describe_pet(animal_type='fish',pet_name='gold fish')