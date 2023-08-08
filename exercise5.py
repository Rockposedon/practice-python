'''
  Python script to demonstrate finding the intersection of two sets created from lists
'''
# Define two lists
list1 = [1, 2, 3, 4, 5, 5, 5, 6, 78]
list2 = [1, 2, 3, 4, 5, 5, 53, 2, 1, 90]

# Create sets from the lists to remove duplicates
set1 = set(list1)
set2 = set(list2)

# Find the intersection of the two sets (common elements)
intersection_result = set1.intersection(set2)

# Print the intersection result
print("Intersection of set1 and set2:", intersection_result)
