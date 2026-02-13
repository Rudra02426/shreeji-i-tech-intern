### Task 10: `filter()` Function

def even_num(a):
	return a %2 == 0
num=[1, 2, 3 ,4]
result=list(filter(even_num ,num))
print(result)