class Car():
	"""docstring for Car"""
	def __init__(self, make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_distriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self,miles):
		if miles >= self.odometer_reading:
			self.odometer_reading = miles
		else:
			print("You can't roll back odometer.")

	def intrement_odometer(self,miles):
		self.odometer_reading += miles