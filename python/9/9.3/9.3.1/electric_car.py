class Car():
	"""docstring for Car"""
	def __init__(self, make,model,year):
		
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self,miles):
		if miles >= self.odometer_reading:
			self.odometer_reading = miles
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self,miles):
		self.odometer_reading += miles

# 创建子类时，父类必须包含在当前文件中，肯位于子类前面
# 定义子类时，必须在括号内指定父类的名称。
class ElectricCar(Car):
	"""电动汽车的独特之处"""
	def __init__(self, make,model,year):
		"""初始化父类的属性"""
		super().__init__(make,model,year)
		# super()是一个特殊函数，帮助Python将父类和子类关联起来。

my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())