# Car类的代码
class Car():
	"""一次模拟汽车的简单尝试"""
	def __init__(self, make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")
	def update_odometer(self,mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	def increment_odometer(self,miles):
		self.odometer_reading += miles

# 创建子类时，父类必须包含在当前文件中，且位于子类前面。
# 此处定义了子类ElectricCar。定义子类时，必须在括号内指定父类的名称。
class ElectricCar(Car):
	"""电动汽车的独特之处"""
	"""Reoresent aspects of a car,specific to electric vehicles."""
	def __init__(self, make,model,year):	#方法__init__()接受创建Car实例所需的信息。
		
		"""初始化父类的属性"""
		# super()是一个特殊函数，帮助Python将父类和子类关联起来。这行代码让Python调用ElectricCar的父类的方法__init__()，让ElectricCar实例包含父类的所有属性
		"""
		电动汽车的独特之处
		初始化父类的属性，再初始化电动汽车特有的属性
		"""
		super().__init__(make,model,year)
		self.battery_size = 70	# 添加了新属性self.battery_size，并给定初始值70
	def describe_battery(self): # 添加了一个人名为describe_battery()的方法，它打印有关电瓶的信息
		"""打印一条描述电瓶容量的消息"""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")

# 创建ElectricCar类的一个实例，并将其存储在变量my_tesla中。
# 这行代码调用ElectricCar类中定义的方法__init__()，后者让Python调用父类Car中定义的方法__init__()
my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
		