# Task 14: Find Largest Element

lis=[ 10, 15, 22, 90, 33]
large=lis[0]
for i in lis:
	if i>large:
		large = i
print("largest element is:" ,large)