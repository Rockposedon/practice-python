def take_choice():
    choice = input("enter y for yes and n for no : ")
    if choice == "y" or choice == "Y":
        return True
    elif choice == "n" or choice == "N":
        return False
    else :
        print("invalid choice ")
        take_choice()


user_choice = take_choice()

# Print the user's choice
print("User's choice:", user_choice)
