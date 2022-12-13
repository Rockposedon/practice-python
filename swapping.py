#swapping of program
#in three wayss
#taking addition variable
v1 = 1
v2 = 20
temp = v1
v1 = v2
v2 = temp
print("v1,v2,temp = ", v1,v2,temp)
print("----------------------------------------------")
# another way to solve 
#without takking addition
a = 1
b = 20
print(a,b)
a=a+b
b=a-b
a=a-b
print(a,b)
print("-----------------------------------------------")

#another way
#python special
c = 20
d = 90
print(c,d)
a,b = b,a
print(c,d)
print("-----------------------------------------------")
