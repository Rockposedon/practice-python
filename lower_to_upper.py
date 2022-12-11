x = input("enter the values:")
y =" "
for i in x:
	if ord(i)>=65 and ord(i)<=122:
		a = ord(i)-32
		b = chr(a)
		y = y+b
	else:
		y=y+i
print("before = ", x)
print("after = ", y)	    	