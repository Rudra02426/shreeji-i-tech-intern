### Task 15: Operator Overloading
class Num:
	def __init__(self, value):
		self.value = value
	def __add__(self, other):
		return self.value + other.value
a= Num(10)
b= Num(11)
print(a +b )