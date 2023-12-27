# Prompt the user to enter a value
x = int(input("Enter the value = "))

# Initialize a variable 'y' to store the factorial result
y = 1

# Iterate through numbers from 1 to 'x' (inclusive)
for i in range(1, x + 1):
    # Calculate the factorial by multiplying 'y' with the current number 'i'
    y = y * i

# Print the calculated factorial
print("Factorial of {} is {}".format(x, y))
