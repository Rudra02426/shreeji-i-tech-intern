### Task 20: Power of Number

def pwr(x,n):
	if n == 0:
		return 1
	return x * pwr(x, n-1)
x=int(input("enter number : "))
n=int(input("enter number of power: "))
print(pwr(x,n))