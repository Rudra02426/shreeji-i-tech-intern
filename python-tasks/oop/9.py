
### Task 9: Single Inheritance

class Person:
	def __init__(self, name, age):
		self.name=name
		self.age=age
class Employee(Person):
	def __init__(self, name, age, salary):
		super().__init__(name,age)
		self.salary= salary 
name =input("enter your name: ")
age =int(input("enter your age: "))
salary =int(input("enter employee salary: "))
emp = Employee(name, age, salary)
print("name: ", emp.name)
print("age:", emp.age)
print("salary: ", emp.salary)