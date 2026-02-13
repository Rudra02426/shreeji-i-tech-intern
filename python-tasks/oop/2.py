### Task 2: Object Creation
class Student:
	def display_details(self):
		print(f"hello.. {self.name} your age is {self.age}")
stud1=Student()
stud2=Student()
stud1.name="Rudra"
stud1.age=21
stud2.name="Tirth"
stud2.age=22
stud1.display_details()
stud2.display_details()