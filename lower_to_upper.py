'''
	Python script in which each character of the input string converts
 	lowercase letters to uppercase using ASCII values. Other characters
  	are added to the modified string without any change
'''
# Get input string from the user
x = input("Enter the values: ")  
# Initialize an empty string 'y' to store the modified string
y = " "  

# Loop through each character in the input string
for i in x:
    if ord(i) >= 65 and ord(i) <= 122:  # Check if the character is within the range of uppercase and lowercase letters
        a = ord(i) - 32  # Convert lowercase ASCII code to uppercase ASCII code
        b = chr(a)  # Convert ASCII value back to character
        y = y + b  # Append the uppercase character to the 'y' string
    else:
        y = y + i  # Append the character as is to the 'y' string

# Print the original and modified strings
print("Before: ", x)  # Print the original input string
print("After: ", y)  # Print the modified string with uppercase letters
