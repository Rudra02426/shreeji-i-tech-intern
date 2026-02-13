### Task 4: Function with Return Value

def mark(mrk):
	total=sum(mrk)
	avg=total /len(mrk)
	return total, avg
a, b=mark([70, 80, 90])
print("total is: ",a)
print("average is: ", b)