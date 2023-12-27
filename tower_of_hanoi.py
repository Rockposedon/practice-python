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
        if len(self.container) > 0:
            return self.container.pop()
        return None
            

    # def size(self):
    #     # Return the size of the stack
    #     if len(self.container) == 0:
    #         raise Exception("Stack is empty")
    #     else:
    #         return len(self.container)

    def print_stack(self):
        # Return the elements of the stack
        print(self.container)
        return self.container


    def is_empty(self):
        return len(self.stack) == 0

my_stack_1 = Stack()
my_stack_2 = Stack()
my_stack_3 = Stack()

my_stack_1.push("C")
my_stack_1.push("B")
my_stack_1.push("A")

print("Step one :  ")
print(my_stack_3.push(my_stack_1.pop()))
print("Step two : ")
my_stack_2.push(my_stack_1.pop())
print("Step three : ")
my_stack_2.push(my_stack_3.pop())
print("Step four : ")
my_stack_3.push(my_stack_1.pop())
print("Step five : ")
my_stack_1.push(my_stack_2.pop())
print("Step six : ")
my_stack_3.push(my_stack_2.pop())
print("Step seven : ")
my_stack_3.push(my_stack_1.pop())


my_stack_1.print_stack()
my_stack_2.print_stack()
my_stack_3.print_stack()
# def TOH(n,a,b,c):
#     if n == 1:
#         print("move 1 from", a, "to",c)
#     else :
#         TOH(n-1,a,c,b)
#         print("move",n,"from",a , "to",c)
#         TOH(n-1,b,a,c)
# TOH(3,'a','b','c')