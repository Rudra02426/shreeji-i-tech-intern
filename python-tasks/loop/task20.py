### Task 20: Fibonacci Series
num=int(input("enter number:"))
a=0
b=1
for i in range(num):
	print(a, end=" ")
	next=a+b
	a=b
	b=next
	
