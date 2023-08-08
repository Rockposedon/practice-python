''' Problem statement 
    Write Python script to perform basic arithmetic operations as Calculator  
'''

# Take user inputs for variables a and b
a1 = int(input("enter a: "))
b1 = int(input("enter b: "))

# Define function to perform addition
def add(a, b):
    return a + b

# Define function to perform subtraction
def sub(a, b):
    return a - b

# Define function to perform multiplication
def mul(a, b):
    return a * b

# Define function to perform division
def div(a, b):
    return a / b

# Display available operations to the user
print("Please select the operation:")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

# Take user choice as input
choice = input("Please enter choice (a/ b/ c/ d): ")

# Perform the selected operation based on user's choice
if choice == 'a':
    print('addition of a and b :')
    print(add(a1, b1))
elif choice == 'b':
    print('subtraction of a and b :')
    print(sub(a1, b1))
elif choice == 'c':
    print('multiplication of a and b')
    print(mul(a1, b1))
elif choice == 'd':
    print('division of a and b :', div(a1, b1))
