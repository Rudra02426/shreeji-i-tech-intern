### Task 7: Getter & Setter

class BankAccount:
	def __init__(self, balance):
		self.__balance = balance
	def get_balance(self):
		return self.__balance
	def set_balance(self, amount):
		self.__balance += amount

balance=int(input("enter your bank balance: "))
acc = BankAccount(balance)
print("current balance: ", acc.get_balance())
dep=int(input("enter amount for deposite:"))
acc.set_balance(dep)
print("deposite successfull current balance: ",acc.get_balance())