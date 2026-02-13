### Task 18: Fibonacci using Recursion

def fibo(num):
	if num == 0:
		return 0
	if num == 1:
		return 1
	return fibo(num-1) + fibo(num-2)
for i in range(5):
	print(fibo(i), end="")