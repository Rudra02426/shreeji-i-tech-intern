### Task 14: Method Overriding

class Shape:
	def area(self):
		print("area")
class Rectangle(Shape):
	def area(self):
		print("rectangle area")
r = Rectangle()
r.area()