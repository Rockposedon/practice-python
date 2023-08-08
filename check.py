# Define a function to take a choice input from the user
# Python script to show the use of function and conditional statements
def take_choice():
    # Prompt the user to enter a choice (y for yes, n for no)
    choice = input("enter y for yes and n for no : ")
    
    # Check if the choice is "y" or "Y" (indicating "yes")
    if choice == "y" or choice == "Y":
        return True  # Return True if the choice is "y"
    # Check if the choice is "n" or "N" (indicating "no")
    elif choice == "n" or choice == "N":
        return False  # Return False if the choice is "n"
    else:
        print("invalid choice ")
        # If the choice is neither "y" nor "n", print an error message and recursively call the function
        
        take_choice()

# Call the 'take_choice' function to get the user's choice
user_choice = take_choice()

# Print the user's choice
print("User's choice:", user_choice)
