''' problem statement
    Write a Python script to generate the multiplication table of prompt-defined number
'''

# Take user input for the number to generate a multiplication table for
n = int(input("enter number : "))

# Iterate through numbers 1 to 10 to generate the multiplication table
for i in range(1, 11):
    # Calculate the result of the multiplication
    result = i * n
    
    # Print the multiplication equation with comments
    print(n, " X", i, "=", result)
