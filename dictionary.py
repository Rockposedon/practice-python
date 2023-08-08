'''
	This Python script to demonstrates various operations on dictionaries, including adding, modifying,
 	and deleting key-value pairs, as well as access keys, values, and items in a dictionary
'''
# Define a dictionary d1 with key-value pairs
d1 = {"name": "paritosh", "name": "don", "class": "mca", "subject": "science"}

# Print the dictionary (Note: Duplicate keys will be overridden)
print(d1)

# Print keys only using a for loop
print("Keys only:")
for i in d1:
    print(i)

# Print values only using a for loop
print("Values only:")
for i in d1:
    print(d1[i])

# Print items (key-value pairs) using a for loop
print("Items (both):")
for i, j in d1.items():
    print(i)
    print(j)

# Print values using the values() method
print("Values:", d1.values())

# Print items using the items() method
print("Items:", d1.items())

# Print keys using the keys() method
print("Keys:", d1.keys())

# Define another dictionary d2 with key-value pairs (Note: Duplicate keys will be overridden)
d2 = {1: "21", 2: "31", 3: "41", 3: "2121"}

# Print key-value pairs using a for loop
print("Key-value pairs in d2:")
for i, j in d2.items():
    print(i, j)

# Modify the value associated with the "name" key
d1["name"] = "paritosh verma"
print("Modified d1:", d1)

# Add a new key-value pair to d1
d1["school"] = "TKS"
print("Updated d1:", d1)

# Delete a value using its key using the pop() method
d1.pop("school")
print("After deleting 'school':", d1)

# The line 'd1.remove()' is incorrect and will result in an AttributeError
# There is no 'remove' method for dictionaries
