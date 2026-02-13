# Task 7: Count Digits
a=int(input("enter number for count:"))
count=0
while a > 0:
	count += 1
	a //=10
print("total digits are:",count)