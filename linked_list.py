# Creating linked list node class
class Node:

    # Constructor
    def __init__(self,data=None,next = None):
        self.data = data
        self.next = next

# Class to insert element at the start,end and index
class Linked_list:
    
    def __init__(self):
        self.head = None


    # Function to add element in the beginning
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node


    # Function to add element at the end
    def insert_at_end(self,data):

        if self.head is None:
            self.head = Node(data,None)
            return
        itr  = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)


    # Function to find length of linked list
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count


    # Function to add element at specified index
    def insert_at_index(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid Index')
        count = 0 
        itr= self.head
        while itr :
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count  += 1


    # Function to print the linked list
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr  = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)


    # Function to remove element at specific index
    def remove_at_index(self,index):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid Index')
        if index == 0:
            self.head = self.head.next
        count = 0 
        itr= self.head
        while itr :
            if count == index-1:
                
                itr.next = itr.next.next
                break
            itr = itr.next
            count  += 1


    # Function to insert element after value
    def insert_by_value(self,value ,data):
        itr = self.head
        while itr:
            if itr.data == value:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
    

    # Function to remove element by specific value
    def remove_by_value(self, value):
        current = self.head
        previous = None
        while current is not None:
            if current.data == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                break
            previous = current
            current = current.next





ll = Linked_list()

ll.insert_at_beginning(50)
ll.insert_at_beginning(34)
ll.insert_at_beginning(69)
ll.insert_at_beginning(90)

ll.insert_at_end(111)
ll.insert_at_end(321)
ll.insert_at_end(1000)
ll.insert_at_end(2023)

ll.insert_at_index(3,9090)
ll.insert_at_index(7,"index h bhai")
ll.insert_at_index(1,567)
ll.insert_at_index(5,10000)

ll.insert_by_value(90,111)
ll.insert_by_value(1000,9090)
ll.insert_by_value(111,222)

ll.remove_at_index(4)
ll.remove_at_index(5)
ll.remove_at_index(9)
ll.remove_at_index(6)

ll.remove_by_value(567)
ll.remove_by_value(2023)

ll.print()


