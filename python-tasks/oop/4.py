
### Task 4: Instance Method

class stud:
	def __init__(self, age):
		self.age=age
	def adult(self):
		if self.age >=18:
			print("adult")
		else:
			print("not adult")
s=int(input("enter your age to check youre adult or not: "))
s=stud(s)
s.adult()