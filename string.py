name = 'paritosh'
device = "paritosh's iphone"
print(type(name))
print(type(device))
print(device)
print(name)

name = "sunny"
age  = "29"
contact = "123456"
email = "sunnysir@gmail.com"
#normal and simple method

my_intro = ("hi my name is ",name , "i am " , age , "year old", "my phone no. is " , contact, "and email is", email)
print(my_intro)
#using (+) operator
my__details = ("hi my name is "+ name + "i am " + age + "year old" + "my phone no. is " + contact + "and email is" + email)
print(my__details)
#using format operator to reduce complexity
print("hi my name is {}. I am {} years old. My contact number is {}. and email is ." .format(name,age,contact,email))