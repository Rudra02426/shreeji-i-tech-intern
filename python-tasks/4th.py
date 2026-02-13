#list operation

number=[12,11,22,33,24]
print("numbers are: " , number)
number.append(6)
print("after added number: " ,number)
number.remove(11)
print("after remove number: ",number)
number.sort()
print("sorted list:", number)
print("minimum number is:" ,min(number))
print("maximum number is:" ,max(number))
print("addition of numbers is: ", sum(number))