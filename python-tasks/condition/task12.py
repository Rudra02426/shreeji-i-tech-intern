# Task 12: Largest of Three Numbers
num1=int(input("enter 1st number:"))
num2=int(input("enter 2ed number:"))
num3=int(input("enter 3rd number:"))
if num1>num2 and num1>num3:
	print("1st number is greater")
elif num2>num1 and num2>num3:
	print("2ed number is greater")
elif num3>num1 and num3>num2:
	print("3rd number is greater")
else:
	print("all are equal")