# x = input("enter the values:")
# y =" "
# for i in x:
# 	if ord(i)>=65 and ord(i)<=90:
# 		a = ord(i)+32
# 		b = chr(a)
# 		y = y+b
# 	elif ord(i)>=97 and ord(i)<=122:
# 		y = y+i
# 	else:
# 	    print("invalid")
# 	    break
# print("before = ", x)
# print("after = ", y)	    	
x = input("enter the values:")
y =""
for i in x:
	if ord(i)>=65 and ord(i)<=90:
		a = ord(i)+32
		b = chr(a)
		y = y+b
	else:
	    y=y+i
	    
print("before = ", x)
print("after = ", y)	    	