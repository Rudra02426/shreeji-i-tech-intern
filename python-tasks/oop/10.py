### Task 10: Method Overriding
class person:
	def display(self):
		print("this is person ")
class emp:
	def display(self):
		print("this is employee")
per=person()
e=emp()
per.display()
e.display()