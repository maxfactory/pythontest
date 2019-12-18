class Car():
	"""docstring for Car"""
	def __init__(self, make, model, year):
		
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		self.gas_tank = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def fill_gas_tank(self):
		print("This car gas tank is:" + str(self.gas_tank) + "-L")

	def add_gas(self,kilogram):
		if self.gas_tank == 0:
			self.gas_tank += kilogram
		else:
			print("Please fill the gas tank.")

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

	def fill_gas_tank(self):
		"""电动汽车没有油箱"""
		print("This car doesn't need a gas tank!")

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

my_new_car.add_gas(100)
my_new_car.fill_gas_tank()

my_tesla = EletricCar('tesla','model s',2016)
print("\n" + my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank()