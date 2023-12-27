'''
	Check given string is palindrome or not 	
'''
# Prompt the user to enter a string
s1 = input("enter the string : ")

# Check if the input string is equal to its reverse
if s1 == s1[::-1]:
    print(s1, " is palindrome")
else:
    print(s1, "is not a palindrome")
