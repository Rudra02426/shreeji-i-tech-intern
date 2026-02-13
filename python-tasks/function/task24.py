### Task 24: Nested Function

def result(mrk1, mrk2):
	def operation():
		print("total is",mrk1 + mrk2)
	operation()
mrk1=int(input("enter 1st mark:"))
mrk2=int(input("enter 2ed mark:"))
result(mrk1,mrk2)

		