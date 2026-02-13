### Task 6: Public & Private Variables

class BankAccount:
	def __init__(self, name, balance):
		self.name = name
		self.__balance = balance
	def deposit(self, amount):
		self.__balance += amount
		print("deposit successfull")
	def withdraw(self, amount):
		if amount < self.__balance:
			self.__balance -= amount
			print("withdraw successfull")
		else:
			print("insufficient balance")
	def show_balance(self):
		print("current balance is : ", self.__balance)
name=input(" enter account holder name: ")
balance=int(input("enter your bank balance: "))
acc = BankAccount(name, balance)
print("accont holder is :", acc.name)
acc.show_balance()
dep=int(input("enter amont for deposite: "))
acc.deposit(dep)
acc.show_balance()
wd=int(input("enter amont for withdraw: ")) 
acc.withdraw(wd)
acc.show_balance()