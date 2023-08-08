'''
	Python script which processes each character of the input string and either converts 
 	uppercase letters to lowercase or leave lowercase and other characters unchanged
'''

# Get input string from the user
x = input("Enter the values: ")  
# Initialize an empty string 'y' to store the modified string
y = " "  

for i in x:
    if ord(i) >= 65 and ord(i) <= 90:  # Check if character is uppercase
        a = ord(i) + 32  # Convert uppercase to lowercase using ASCII values
        b = chr(a)  # Convert ASCII value back to character
        y = y + b  # Append the lowercase character to the 'y' string
    elif ord(i) >= 97 and ord(i) <= 122:  # Check if character is already lowercase
        y = y + i  # Append the lowercase character to the 'y' string
    else:
        print("Invalid character")
        break  # Exit the loop if an invalid character is encountered

print("Before: ", x)  # Print the original input string
print("After: ", y)  # Print the modified string with lowercase letters
