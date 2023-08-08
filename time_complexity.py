'''
	You are required to create a Python program that calculates the factorial 
 	of a given number using a recursive function. Additionally, the program 
  	should measure the time taken for the execution of the factorial calculation
   	and provide this timing information to the user
'''

# Import the time module to measure execution time
from time import *

# Define a recursive function to calculate the factorial of a number
def fact(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * fact(x - 1)

# Get user input for the value for which to calculate the factorial
var1 = int(input("Enter a value: "))

# Record the start time of the execution
start_time = time()

# Calculate the factorial of the input value using the 'fact' function
result = fact(var1)

# Display the calculated factorial
print("Factorial of {} is {}".format(var1, result))

# Record the end time of the execution
end_time = time()

# Calculate the total time taken for the program execution
total = end_time - start_time

# Display the total execution time
print("Total time for execution of program:", total)
