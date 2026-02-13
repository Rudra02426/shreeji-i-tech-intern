# Task 13: Count Even & Odd

lis=[1,2,3,4,5,6]
even=0
odd=0
for i in lis:
	if i %2==0:
		even += 1
	else:
		odd += 1
print("even numbers :", even)
print("odd numbers:", odd)