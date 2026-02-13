### Task 17: Sum of Digits

def add(num):
	if num == 0:
		return 0
	return num % 10 + add(num // 10)
print(add(111111111111))