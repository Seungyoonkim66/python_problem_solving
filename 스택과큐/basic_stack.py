class Stack:
    def  __init__ (self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self)->int:
        if self.is_empty(): 
            print("Stack is empty!")
            return None
        else:
            return self.stack.pop()
    
    def check_top(self)->None:
        if self.is_empty(): 
            print("Stack is empty!")
            return None
        else:
            return self.stack[-1]

    def is_empty(self)-> bool:
        if len(self.stack) == 0:
            return True
        else : 
            return False
    
    def print_stack(self)->None:
        print("Stack Status : TOP[ ", end = "" )
        for i in self.stack:
            print(i, end=" ")
        print("]BOTTOM")