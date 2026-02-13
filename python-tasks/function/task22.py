### Task 22: Recursion vs Loop
#loop

facto= 1
n=5
for i in range(1,n+1):
	facto *= i
print(facto)

#recursion

def fac(n):
	if n == 1:
		return 1
	return n * fac(n-1)
print(fac(5))


