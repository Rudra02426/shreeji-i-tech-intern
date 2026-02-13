# Task 14: Simple Calculator
a=int(input("enter 1st number:"))
b=int(input("enter 2ed number:"))
op=input("enter operation +,-,*,/ : ")
if op == "+":
	op=a+b
	print("addition is :",op)

elif op == "-":
	op=a-b
	print("substaction is :",op)

elif op == "*":
	op=a*b
	print("multiplication is :",op)

elif op =="/":
	op=a/b
	print("division is :",op)

else:
	print("please select +,-,* or /")