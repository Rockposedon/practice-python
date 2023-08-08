<--------------------pattern 1---------------------->
# Get input from the user for the number
num = int(input("Enter a number: "))

# Outer loop for iterating through numbers from 1 to num (inclusive)
for n in range(1, num+1):
    # Inner loop for printing numbers in decreasing order
    for i in range(n, 0, -1):
        print(i, end=" ")  # Print the current number and a space
    print("")  # Move to the next line after each inner loop completes
'''
        1 
        2 1 
        3 2 1 
        4 3 2 1 
        5 4 3 2 1 

'''

<--------------------pattern 2---------------------->
# Get input from the user for the number
num = int(input("Enter a number: "))

# Outer loop for iterating through numbers from 1 to num (inclusive)
for n in range(1, num+1):
    # Inner loop for printing numbers in decreasing order
    for i in range(0, n+1):
        for j in range(i, 0, -1):
            print(j, end=" ")  # Print the current number and a space
        print("")  # Move to the next line after each inner loop completes
'''
         
        1 
        2 1 
        3 2 1 
        4 3 2 1 

'''
<--------------------pattern 3---------------------->

# Get input from the user for the number
num = int(input("Enter a number: "))

# Outer loop for iterating through numbers from 1 to num (inclusive)
for n in range(1, num+1):
    # Inner loop for printing numbers in decreasing order
    for i in range(n, 0, -1):
        print(i, end=" ")  # Print the current number and a space
    print("")  # Move to the next line after each inner loop completes

'''
            1
           22
          333
         4444
        55555

'''

<--------------------pattern 4---------------------->
# Get input from the user for the number of rows
rows = int(input("Enter value: "))

# Outer loop for rows
for row in range(1, rows+1):
    num = 1  # Initialize the number to be printed
    # Inner loop for columns
    for j in range(rows, 0, -1):
        if j > row:
            print(" ", end=" ")  # Print space if the column number is greater than the current row number
        else:
            print(num, end=" ")  # Print the number and increment it
            num += 1
    print(" ")  # Move to the next line after printing each row


'''
            1  
          1 2  
        1 2 3  
      1 2 3 4  
    1 2 3 4 5  
     
'''
