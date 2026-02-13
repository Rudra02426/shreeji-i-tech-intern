#task10 electricity bill count
unit=int(input("enter used units:"))
if unit<=100:
	total=unit * 5
elif unit <=200:
	total=unit * 7
else:
	total=unit*10
print("total bill is:",total)