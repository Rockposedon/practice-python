'''
      Fetch even elements from the list and print even list
'''
# Given a list of numbers
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Create a new list 'l1' using a list comprehension
l1 = [i for i in a if i % 2 == 0]

# Print the new list containing even numbers
print(l1)
