'''
	check the given string is palindrome or not 
'''
# Get input from the user
name = input("Enter a string: ")

# Check if the input string is the same as its reverse
if name == name[::-1]:
    print(name, "is a palindrome.")
else:
    print(name, "is not a palindrome.")
