'''
        Python script to define a calculator function that takes user inputs 
        for two values and a choice of operation. It performs the selected 
        operation and displays the result
'''

# Creating calculator function named 'cal'
def cal():
    print("Welcome to my calculator")
    
    # Get user inputs for two values and the operation choice
    var1 = int(input("Enter value 1: "))
    var2 = int(input("Enter value 2: "))
    
    # Display choices for different operations
    print("Enter 1 for addition")
    print("Enter 2 for subtraction")
    print("Enter 3 for multiplication")
    print("Enter 4 for division")
    print("Enter 5 for power")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        result = var1 + var2
        print("Result =", result)
    elif choice == '2':
        result = var1 - var2
        print("Result =", result)
    elif choice == '3':
        result = var1 * var2
        print("Result =", result)
    elif choice == '4':
        result = var1 / var2
        print("Result =", result)
    elif choice == '5':
        result = var1 ** var2
        print("Result =", result)
    else:
        print("Invalid choice. Please enter a valid option.")
        cal()  # Recursively call the cal() function to restart the calculator

# Call the calculator function to start the calculator
cal()
