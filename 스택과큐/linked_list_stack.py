class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def  __init__ (self):
        self.top = None
    
    def push(self, data)->None:
        new_node = Node(data)
        if not self.is_empty():
            new_node.next = self.top
        self.top = new_node
            
    def pop(self)->(int or None):
        if self.is_empty():
            return None
        else :
            popped = self.top.data
            self.top = self.top.next
            return popped
    
    def check_top(self)->(int or None):
        if self.is_empty():
            return None
        else : 
            return self.top.data
    
    def is_empty(self)->bool:
        if self.top == None:
            return True
        else:
            return False
    
    def print_stack(self)->None:
        if self.is_empty():
            print("Stack is Empty!")
        else:
            print("Stack Status : TOP[ ", end = "")
            current_node = self.top
            while current_node:
                print(current_node.data, end = " ")
                current_node = current_node.next
            print("]BOTTOM")

    def stack_size(self) -> int:
        current_node = self.top
        size = 0
        while current_node:
            size += 1
            current_node = current_node.next
        return size
            
            
