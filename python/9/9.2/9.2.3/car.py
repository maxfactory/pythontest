## 修改属性的值

# 1、直接修改属性的值
# class Car():
# 	"""docstring for Car"""
# 	def __init__(self,make,model,year):
		
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 		self.odometer_reading =0

# 	def get_descriptive_name(self):
# 		long_name = str(self.year) +' ' + self.make + ' ' + self.model
# 		return long_name.title()

# 	def read_odometer(self):
# 		print("This car has " + str(self.odometer_reading) + " miles on it.")

# my_new_car = Car('audi','a4',2016)
# print(my_new_car.get_descriptive_name())

# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()
#---------------------------------------------------

#通过方法修改属性的值
# class Car():
# 	"""docstring for Car"""
# 	def __init__(self, make,model,year):
		
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 		self.odometer_reading = 0

# 	def get_descriptive_name(self):
# 		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
# 		return long_name.title()

# 	def read_odometer(self):
# 		print("This car has " + str(self.odometer_reading) + " miles on it.")

# 	def update_odometer(self,mileage):
# 		self.odometer_reading = mileage

# my_new_car = Car('audi','a4',2016)
# print(my_new_car.get_descriptive_name())

# my_new_car.update_odometer(23)
# my_new_car.read_odometer()
#--------------------------------------

# 禁止任何人将里程表读数往回调
# class Car():
# 	"""docstring for Car"""
# 	def __init__(self, make,model,year):
		
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 		self.odometer_reading = 0

# 	def get_descriptive_name(self):
# 		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
# 		return long_name.title()

# 	def read_odometer(self):
# 		print("This car has " + str(self.odometer_reading) + " miles on it.")

# 	def update_odometer(self,mileage):
# 		if mileage >= self.odometer_reading:
# 			self.odometer_reading = mileage
# 		else:
# 			print("You can't roll back an odometer!")
#------------------------------------------------------

#通过方法对属性的值进行递增
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

	def update_odometer(self,mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self,miles):
		"""将里程表读数增加指定的量"""
		self.odometer_reading += miles

my_used_car = Car('subaru','outback',2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()