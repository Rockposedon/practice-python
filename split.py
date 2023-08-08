'''
	You are tasked with creating a Python program that takes a paragraph as input
 	and splits it into individual sentences. Each sentence is separated by a period 
  	('.') and should be printed on a new line
'''

# Get input from the user
user_string = input("Enter a string: ")

# Initialize an empty string variable 'x'
x = " "

# Loop through each character in the input string
for i in user_string:
    if i == ".":
        # If a dot is encountered, print the current value of 'x'
        print(x)
        # Reset 'x' to an empty string for the next part of the sentence
        x = " "
    else:
        # Add the current character to 'x'
        x = x + i

# Print the last value of 'x' after the loop completes
print(x)
