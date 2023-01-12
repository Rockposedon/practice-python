a1 = int(input("enter a: "))
b1 = int(input("enter b: "))
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return(a/b)

print("Please select the operation:")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

choice = input("Please enter choice (a/ b/ c/ d): ")

if choice == 'a':
    print('addition of a and b :')
    print(add(a1,b1))
elif choice == 'b':
    print('subtraction of a and b :')
    print(sub(a1,b1))
elif choice == 'c':
    print('multiplication of a and b')
    print(mul(a1,b1))
elif choice == 'd':
    print('division of a and b :',div(a1,b1))
