### Task 5: Class Variable

class College:
	college_Name = "sarvodaya college"
	def __init__(self, student_name, course):
		self.student_name=student_name
		self.course= course
nm=input("enter your name: ")
crs=input("enter your course name: ")

c = College(nm , crs)

print(f" hello..{c.student_name} your course is {c.course} in {c.college_Name}")