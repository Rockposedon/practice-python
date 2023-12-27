from collections import deque
import cProfile

class Stack:
    def __init__(self) -> None:

        self.stack = deque()
        self.min_stack = deque()

    def push(self, val):
        # Push the values
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def peek(self):
        # Return the top element of the stack
        return self.stack[-1]

    def pop(self):
        # Pop and return the top element of the stack
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def min_element(self):
        print(self.min_stack[-1])
        return self.min_stack[-1]
    


# Create a stack and test the functionality
m = Stack()
m.push(89)
m.push(2)
m.push(10)
m.push(99)
m.push(12)
m.push(90)


# Find the minimum element in the stack
m.min_element()

'''
Measuring time complexity

import cProfile

def profile_code():
    # Your code to be profiled
    m = Stack()
    m.push(42)
    m.pop()
    m.min_element()

cProfile.run('profile_code()')

'''