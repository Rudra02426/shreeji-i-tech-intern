### Task 11: Multilevel Inheritance3

class vehical:
	def ride(self):
		print(" ride vehical ")

class car(vehical):
	def drive(vehical):
		print(" drive car ")
class ElectricCar(car):
	def charge(self):
		print(" charge electic car ")
ec=ElectricCar()
ec.ride()
ec.drive()
ec.charge()