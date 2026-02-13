### Task 25: Real-Life UDF

def acc(balance, withdraw):
	if withdraw <= 0:
		return "invalid amount......."
	elif withdraw > balance:
		return "insufficient balance...."
	else:
		balance -= withdraw
		return f" withdraw successfully... your current balance is {balance}"
balance=int(input("enter your balance: "))
withdraw=int(input("enter withdraw amount: "))
print(acc(balance,withdraw))