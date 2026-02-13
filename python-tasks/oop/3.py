### Task 3: Constructor (`__init__`)
class Student:
	def __init__(self,name,roll_no):
		self.name=name
		self.roll_no=roll_no
	def display(self):
		print(f" helloo.. {self.name} your roll_no is {self.roll_no}")
stud=Student("Rudra", 1)
stud.display()