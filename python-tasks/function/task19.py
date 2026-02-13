### Task 19: Reverse String

def reverse(strn):
	if strn=="":
		return strn
	return reverse(strn[1:]) + strn[0]
print(reverse("reverse string"))