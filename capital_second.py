value_1 = input("enter the string = ")
value = " "
for i in range(len(value_1)):
	if i != 1 :
		value = value + value_1[i].lower()
	else :
	    value = value + value_1[i].upper()	

print("user given value = " , value_1)
print("camel =" , value)









