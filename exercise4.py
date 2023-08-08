'''
	Python script to find all the divisors of 'x'
'''
# Prompt the user to enter a number and convert the input to an integer
x = int(input("Enter a number: "))

# Create an empty list to store divisors
div = []

# Iterate through numbers from 1 to x (inclusive)
for y in range(1, x+1):
    # Calculate the integer division of x by y
    a = int(x / y)
    
    # Check if x is evenly divisible by y (no remainder)
    if x - a * y == 0:
        # If evenly divisible, add y to the 'div' list
        div.append(y)

# Print the list of divisors
print(div)
