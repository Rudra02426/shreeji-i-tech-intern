#task8 character type
ch=input("enter character :")
if ch.isalpha():
	print("character is alphabet")
elif ch.isdigit():
	print("character is digit")
else:
	print("special character")