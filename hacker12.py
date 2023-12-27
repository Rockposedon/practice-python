'''
    Python function that takes an input string, a position, and a character. 
    The function replaces the character in the input 
    string at the specified position and returns an updated string
'''
def mutate_string(string, position, character):
    # Function to mutate the input string by replacing the character at the given position.

    l = list(string)        # Convert the input string to a list of characters.
    l[position] = character  # Replace the character at the specified position with the new character.
    string = ''.join(l)      # Convert the list back to a string.
    return string           # Return the updated string.

if __name__ == '__main__':
    s = input()              # Read the original string from the user.
    i, c = input().split()   # Read the position and character to replace from the user.
    s_new = mutate_string(s, int(i), c)  # Call the mutate_string function.
    print(s_new)             # Print the updated string.
