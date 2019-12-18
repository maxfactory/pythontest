# 给子类定义属性和方法
class Car():
	"""docstring for Car"""
	def __init__(self, make, model, year):
		
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
			print("You can't roll back odometer!")

	def increment_odometer(self,miles):
		self.odometer_reading += miles

class EletricCar(Car):
	"""docstring for EletricCar"""
	def __init__(self, make,model,year):
		super().__init__(make,model,year)
		self.battery_size = 70

	def describe_battery(self):
		"""打印一条描述电瓶容量的信息"""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")

my_tesla = EletricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())

my_tesla.describe_battery()