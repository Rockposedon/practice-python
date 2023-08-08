'''
	find the given number is odd or even	
'''
# Prompt the user to enter a number and convert the input to an integer
a = int(input("enter the number : "))

# Calculate the remainder when 'a' is divided by 2
condition = a % 2

# Check if the remainder is greater than 0
if condition > 0:
    print("number is odd")
else:
    print("number is even")
