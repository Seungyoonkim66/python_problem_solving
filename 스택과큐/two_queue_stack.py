import linked_list_queue

class Stack:
    def __init__(self) -> None:
        self.inq = linked_list_queue.Queue()
        self.outq = linked_list_queue.Queue()

    def is_empty(self) -> bool:
        if self.inq.queue_size() == 0:
            return True
        else:
            return False

    def push(self, data) -> None:
        self.inq.enqueue(data)
    
    def pop(self) -> int or None:
        if self.is_empty():
            return None
        
        while self.inq.queue_size() != 1:
            self.outq.enqueue(self.inq.dequeue())
        
        result = self.inq.dequeue()
        self.inq, self.outq = self.outq, self.inq

        return result

    def check_top(self) -> int or None:
        if(self.is_empty()):
            return None
        while self.inq.queue_size() != 0:
            self.outq.enqueue(self.inq.dequeue())

        result = self.outq.tail.data
        self.inq, self.outq = self.outq, self.inq
        return result

    def print_stack(self) -> None:
        while self.inq.queue_size() != 0:
            self.outq.enqueue(self.inq.dequeue())
        
        print("BOTTOM [ ", end="")
        while self.outq.queue_size() != 0:
            popped = self.outq.dequeue()
            self.inq.enqueue(popped)
            print(popped, end=" -> ")
        print(" ] TOP")
        


# s = Stack()

# for i in range(1, 20, 2):
#     s.push(i)

# # for i in range(1, 20, 2):
# #     print(s.pop(), end=" ")

# s.print_stack()
# print(s.check_top())