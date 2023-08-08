# Define a string variable 'name'
name = 'paritosh'

# Define a string variable 'device' with an apostrophe within it
device = "paritosh's iphone"

# Print the data type of the 'name' and 'device' variables
print(type(name))
print(type(device))

# Print the 'device' and 'name' variables
print(device)
print(name)

# Overwrite the 'name', 'age', 'contact', and 'email' variables with new values
name = "sunny"
age = "29"
contact = "123456"
email = "sunnysir@gmail.com"

# Create a string using a tuple and the '+' operator
my_intro = ("hi my name is ", name, "i am ", age, "years old", "my phone no. is ", contact, "and email is", email)
print(my_intro)

# Create a string using the '+' operator
my_details = ("hi my name is " + name + "i am " + age + " years old" + " my phone no. is " + contact + " and email is" + email)
print(my_details)

# Create a string using the format operator to reduce complexity
print("hi my name is {}. I am {} years old. My contact number is {}. and email is {}." .format(name, age, contact, email))
