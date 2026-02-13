# Task 10: Prime Number

a=int(input("enter number to check prime number:"))
prm=True
if a<=1:
	prm= False
else:
	for i in range(2, a):
		if a % i == 0:
			prm=False
			break
if prm:
	print("prime number ")
else:
	print("not a prime number")