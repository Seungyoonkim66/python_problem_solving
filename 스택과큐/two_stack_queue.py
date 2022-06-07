import linked_list_stack

class Queue:

    def __init__(self):
        self.in_stack = linked_list_stack.Stack()
        self.out_stack = linked_list_stack.Stack()
    
    def enqueue(self, data) -> None:
        self.in_stack.push(data)

    def dequeue(self) -> int or None:
        if self.in_stack.is_empty():
            print("Queue is Empty")
            return None
        
        while self.in_stack.stack_size() != 1:
            self.out_stack.push(self.in_stack.pop())
        
        result = self.in_stack.pop()

        self.in_stack, self.out_stack = self.out_stack, self.in_stack
        return result

    

# q = TwoStackQueue()
# for i in range(1,6,1):
#     q.enqueue(i)

# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())