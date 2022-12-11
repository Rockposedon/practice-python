#split string when dot come in string 
user_string = input("enter string")
x= " "
for i in user_string:
	if i == ".":
		print(x)
		x = " "
	else:
		x = x+i
print(x)
    	