### Task 8: Data Hiding
#try to access local var globally
class Acc:
	def __init__(self,balance):
		self.__balance= balance #private
	def get_balance(self):
		return self.__balance
amnt= Acc(500)
print("balance: ", amnt.get_balance())
print(amnt.__balance)

#AttributeError: 'Acc' object has no attribute '__balance'. Did you mean: 'get_balance'?
#can't use private var globally