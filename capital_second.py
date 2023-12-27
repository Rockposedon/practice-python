# Prompt the user to input a string
value_1 = input("enter the string = ")

# Initialize an empty string 'value' to store the modified string
value = " "

# Iterate through each character in the input string
for i in range(len(value_1)):
    # Check if the current character is not the first character (at index 0)
    if i != 0:
        # Convert the character to lowercase and append it to the 'value' string
        value = value + value_1[i].lower()
    else:
        # Convert the first character to uppercase and append it to the 'value' string
        value = value + value_1[i].upper()

# Print the original user-given value
print("user given value =", value_1)

# Print the modified 'camel' string
print("camel =", value)
