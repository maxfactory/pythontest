# 创建一个Dog类
class Dog():
	"""一次模拟小狗的简单尝试"""
	def __init__(self,name,age):
		# 创建Dog实例时，Python将调用Dog类的方法__init__()。
		"""初始化属性name和age"""
		self.name = name	# 定义两个变量，以solf为前缀的变量都可供类中的所有方法使用，
		self.age = age		#还可以通过类的任何实例来访问这些变量。
	
	def sit(self):
		"""模拟小狗被命令时蹲下"""
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		"""模拟小狗被命令时打滚"""
		print(self.name.title() + " rolled over!")

# 根据类创建实例
my_dog = Dog('willie',6)
# 使用my_dog.name来访问my_dog的属性name的值：在这里，Python先找到实例my_dog
# 再查找与这个实例相关联的属性name。在Dog类中引用这个属性时，使用的是self.name
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()

# 创建多个实例
my_dog = Dog('willie',6)
your_dog = Dog("lucy",3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.roll_over()