# Filtering and printing elements from a list 

# Define a list named 'list1' with various elements
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 2.3, 2.3344, 9.7]

# Print the entire list
print("Original list:", list1)

# Check each element in the list and print elements greater than 5
print("Elements greater than 5:")
for element in list1:
    if element > 5:
        print(element)

# Iterate through the list and print elements less than 5
print("Elements less than 5:")
for i in list1:
    if i < 5:
        print(i)
