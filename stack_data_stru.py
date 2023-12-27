from collections import deque

class Stack:
    def __init__(self) -> None:
        # Initialize the stack using a deque container
        self.container = deque()

    def push(self, val):
        # Push the value onto the stack
        self.container.append(val)

    def peek(self):
        # Return the top element of the stack without removing it
        return self.container[-1]

    def pop(self):
        # Pop and return the top element of the stack
        if len(self.container) == 0:
            print("stack is empty")
        else:
            return self.container.pop()

    def size(self):
        # Return the size of the stack
        if len(self.container) == 0:
            raise Exception("Stack is empty")
        else:
            return len(self.container)

    def print_stack(self):
        # Return the elements of the stack
        return self.container

# Get input from the user
str_input = input("Enter the string: ")

# Create a stack instance
my_stack = Stack()

# Push each character of the input string onto the stack
for char in str_input:
    my_stack.push(char)

# Get the size of the stack
size_of_stack = my_stack.size()

# Print the size of the stack
print("Size of the stack:", size_of_stack)

# Pop and print each element of the stack
for i in range(size_of_stack):
    print(my_stack.pop())
