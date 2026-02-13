# Task 15: Search Element
lis=[1,2,3,4,5]
srh=int(input("enter number to find :"))
find=False
for i in lis:
	if i == srh:
		find=True
		break
if find:
	print("founded",srh)
else:
	print("not founded", srh)