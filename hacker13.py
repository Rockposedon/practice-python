'''
    Python script to capitalize the first letter of an input string and output the modified string
'''

import math
import os
import random
import re
import sys

# Define the function to capitalize the first letter of a string
def solve(s):
    s = s.capitalize()  # Capitalize the first letter of the input string
    return s            # Return the modified string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open an output file for writing

    s = input()           # Read the input string from the user

    result = solve(s)     # Call the solve function to capitalize the string

    fptr.write(result + '\n')  # Write the modified string to the output file

    fptr.close()  # Close the output file
