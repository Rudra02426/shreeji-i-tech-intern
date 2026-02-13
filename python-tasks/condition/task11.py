#task11 atm withdraw
balance=int(input("enter bank balance:"))
withdraw=int(input("enter amount for withdraw:"))
if balance < 500:
	print("minimul balance should be 500")
elif withdraw %100 != 0:
	print("amount will be multiple of 100")
elif withdraw > balance:
	print("amount should not excced of total balance")
else:
	balance=balance-withdraw
	print("successfully withdrawal amount")
	print("available balance is :" , balance) 
