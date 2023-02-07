def myfumction():
    global i
    x = int(input("enter value:"))
    y = int(input("enter value:"))
    z = x+y
    print(z)
    i = "i am in"
    print(id(i))
i = "im outside "
print(id(i))
print(i)
myfumction()
print(i)
