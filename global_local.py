'''
    Python script to demonstrate how the global variable i can be accessed 
    and modified both inside and outside the function's scope, and how 
    local variables within the function do not affect the global variable 
    unless explicitly declared with the global keyword.
'''

# Define a function named 'myfunction'
def myfunction():
    # Declare the global variable 'i' within the function
    global i
    
    # Prompt the user to enter two values
    x = int(input("enter value: "))
    y = int(input("enter value: "))
    
    # Calculate the sum of the entered values
    z = x + y
    
    # Print the sum
    print(z)
    
    # Modify the global variable 'i'
    i = "i am in"
    
    # Print the memory address of 'i'
    print(id(i))

# Initialize the global variable 'i' outside the function
i = "I'm outside"

# Print the memory address and value of 'i'
print(id(i))
print(i)

# Call the 'myfunction' function
myfunction()

# Print the modified global variable 'i'
print(i)
