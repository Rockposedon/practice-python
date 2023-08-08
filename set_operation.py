# Create a set named 'star' containing various data types
star = {2, 4, 6, 2, 10, 12, "yes", "no", 2.4, 233, 0+1j}

# Create a set named 'star1' using a constructor and add an element to it
star1 = set((2, 4, 6, 2, 10, 12))
star1.add("12222")

# Add an element to the 'star' set
star.add("12222")

# Remove an element from the 'star1' set using the 'pop' method
star1.pop()

# Remove an element from the 'star' set using the 'remove' method
star.remove("yes")

# Attempt to remove an element from the 'star' set using 'remove', but it's not present
# Use 'discard' to safely remove an element even if it's not present
star.discard("yes")
star.remove("yes")  # This will raise an error since "yes" was removed earlier

# Print the contents of both sets after performing operations
print(star1)
print(star)
