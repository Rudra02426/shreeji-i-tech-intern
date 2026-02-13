
### Task 13: Method Overloading (Logical)

def addition(*args):
	total=0
	for i in args:
		total += i
	return total
print(addition(1,2,3))
print(addition(1,2,3,4))
print(addition(1,2,3,4,5))

#with use of args sum multiple argument in single mehod