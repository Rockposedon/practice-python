'''
  python script calculate the year in which the user will turn 100 years old
'''
# Prompt the user to enter their name
name = input("enter the name :")

# Prompt the user to enter their age and convert the input to an integer
age = int(input("enter the age : "))

# Calculate the year in which the user will turn 100 years old
year = 2003 - age + 100

# Print a message indicating when the user will be 100 years old
print(name, "u will be 100 in the year", year)
