class Dog():
	"""一次模拟小狗的简单尝试"""
	def __init__(self,name,age):
		"""初始化name和age"""
		self.name = name
		self.age = age

	def sit(self):
		"""模拟小狗被命令时蹲下"""
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		"""模拟小狗被命令时打滚"""
		print(self.name.title() + " rolled over!")

my_dog = Dog('willie',6)  # 实例化

# 创建多个实例
your_dog = Dog('lucy',3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

print("Your dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")


# 根据Dog类创建实例后，就可以使用名点表示法来调用Dog类中定义的任何方法
my_dog.sit()
my_dog.roll_over()

your_dog.sit()
