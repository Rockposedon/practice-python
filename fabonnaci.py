'''
        Python script generates and prints the Fibonacci sequence up to the specified range 'Number' using the iterative approach
'''
# Prompt the user to enter the range for generating the Fibonacci sequence
Number = int(input("Enter the Range: "))

# Initialize variables for the first two values in the Fibonacci sequence
First_Value = 0
Second_Value = 1

# Initialize a counter 'i' to keep track of the current position in the sequence
i = 0

# Iterate while 'i' is less than the specified range 'Number'
while i < Number:
    # For the first two positions, 'Next' is assigned the value of 'i'
    if i <= 1:
        Next = i
    else:
        # Calculate the next value in the sequence as the sum of the previous two values
        Next = First_Value + Second_Value
        
        # Update the 'First_Value' and 'Second_Value' for the next iteration
        First_Value = Second_Value
        Second_Value = Next
    
    # Print the current value in the sequence
    print(Next)
    
    # Increment the counter 'i'
    i = i + 1
