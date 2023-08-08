''' Problem statement
    Write a Python script to calculate the grades of students
'''

# Importing necessary functions from the mini_sub module
from mini_sub import *

# Define a function to calculate the grade based on the 'total' score
def grade():
    # Check if the 'total' score is greater than 35
    if total > 35:
        print("grade : A+ ")
    # If not, check if the 'total' score is greater than 30
    elif total > 30:
        print("grade : A ")
    # If not, check if the 'total' score is greater than 25
    elif total > 25 :
        print("grade : B ")
    # If not, check if the 'total' score is greater than 20
    elif total > 20 :
        print("grade : C ")
    # If not, and the 'total' score is greater than 0, assign grade 'D'
    elif total > 0 :
        print("grade : D")

# Call the 'grade' function to calculate and print the appropriate grade
grade()
