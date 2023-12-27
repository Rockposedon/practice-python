'''
  Python script which takes user inputs for list insertion and number
  calculation and then displays the factors of the given number 
'''

# Check if the script is being run directly
if __name__ == '__main__':
    # Get input from the user to determine the list size
    N = int(input("Enter the list size: "))
    
    # Create an empty list
    list1 = []
    
    # Get user input for the index to insert an element
    i = int(input("Enter the index to insert at: "))
    
    # Get user input for the element to be inserted
    element = input("Enter the value to insert: ")
    
    # Insert the element at the specified index
    list1.insert(i, element)

# Get input from the user to determine a number
numb = int(input("Enter a number: "))

# Create an empty list to store factors
facts = []

# Loop through numbers from 1 to numb (inclusive)
for a in range(1, numb + 1):
    if numb % a == 0:
        # If 'a' is a factor of 'numb', append it to the facts list
        facts.append(a)

# Print the factors of the input number
print("Factors of {} = {}".format(numb, facts))

# Assign the facts list to variable 'a'
a = facts

# Print the value of 'a'
print("Value of 'a':", a)
