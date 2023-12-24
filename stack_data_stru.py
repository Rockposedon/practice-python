from collections import deque

class stack :
    def __init__(self) -> None:
        self.container = deque()
        

    def push(self,val):
        self.container.append(val)
    
    def peek(self):
        return self.container[-1]
    
    def pop(self):
        if len(self.container) == 0:
            print("stack is empty")
        else :    
            return self.container.pop()
    
    def size(self):
        if len(self.container) == 0:
            raise Exception("Stack is empty")
        else:
            return len(self.container)

    def p(self):
        return self.container


str = input("enter the string:")
my_stack = stack()

for char in str:
    my_stack.push(char)

size = my_stack.size()
print(size)

for i in range(size):
    print(my_stack.pop())
