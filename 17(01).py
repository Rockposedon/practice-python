# First approach to determine if a year is a leap year or not
n = int(input("Enter a year: "))  # Prompt the user to input a year

# Check if the year is divisible by 4
if n % 4 == 0:
    print("Year is a leap year")  # Print a message if the year is divisible by 4
    # Check if the year is not divisible by 100
    if n % 100 != 0:
        pass  # No further action is needed for this case
    else:
        # Check if the year is divisible by 400
        if n % 400 == 0:
            print("Year is a leap year")  # Print a message if the year is divisible by 400
        else:
            print("Year is not a leap year")  # Print a message if the year is not divisible by 400
else:
    print("Year is not a leap year")  # Print a message if the year is not divisible by 4



# Another approach to determine if a year is a leap year or not
n = int(input("Enter a year: "))  # Prompt the user to input a year

# Check if the year is divisible by 400 and not divisible by 100
if n % 400 == 0 and n % 100 != 0:
    print("Year is a leap year")  # Print a message if the year meets the condition
# Check if the year is divisible by 4 and not divisible by 100
elif n % 4 == 0 and n % 100 != 0:
    print("Year is a leap year")  # Print a message if the year meets the condition
else:
    print("Year is not a leap year")  # Print a message if the year doesn't meet any condition
