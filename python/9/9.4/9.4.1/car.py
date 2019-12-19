"""一个可用于表示汽车的类"""
class Car():
	"""一次模拟汽车的简单尝试"""
	def __init__(self,make,model,year):
		"""初始化描述汽车的属性"""
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
			print("You can't roll back odometer.")

	def increment_odometer(self,miles):
		self.odometer_reading += miles