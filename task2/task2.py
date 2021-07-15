class Vehicle:
	""" Intialising the vehicle class with color,price and maximum_speed"""
	def __init__(self,color,price,maximum_speed):
		self.color = color
		self.price = price
		self.maximum_speed = maximum_speed


class Car(Vehicle):
	"""Intialsing the car class with tires variable and also intialising parent class vehicle variables"""
	def __init__(self,tires):
		self.tires = tires
		print("Intialsing the Parent class")
		print("****************************")
		i1 = input('Enter the color of vehicle:')
		i2 = input('Enter the price of vehicle: ')
		i3 = input('Enter the max_speed of vehicle: ')
		print("----------------------------")
		super().__init__(i1,i2,i3)

	def __str__(self):
		"""Result of the program"""
		print("Output: ")
		print("*******")
		return f"A {self.color}-colored car with maximum_speed of {self.maximum_speed} km/hr is priced at {self.price} with {self.tires} tires."


print("Intialising the child class")
print("***************************")
no_of_tires = int(input("Enter the number of tires: "))
print("----------------------------")
print("Invoking Child Class Car")
print("************************")
car = Car(no_of_tires)
print(car)