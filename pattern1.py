# Get input from the user
n = int(input("Enter value of n: "))

# Outer loop for rows
for i in range(0, n):
    # Inner loop for columns
    for j in range(0, i + 1):
        print("*", end=" ")  # Print an asterisk and a space without moving to the next line
    print("\r")  # Move to the next line after printing each row

# pattern
'''

    * 
    * * 
    * * * 
    * * * * 
    * * * * *

'''
