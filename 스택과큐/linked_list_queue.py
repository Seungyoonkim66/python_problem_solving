class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def enqueue(self, data) -> None:
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            self.tail = self.tail.next
        
    def dequeue(self) -> int or None:
        if self.head == None:
            print("Queue is Empty")
            return None
        else:
            v = self.head.data
            self.head = self.head.next 

        if self.head == None:
            self.tail = None
        return v
        
    def print_queue(self) -> None:
        current_node = self.head
        string = ""
        while current_node:
            string += str(current_node.data)
            if current_node.next:
                string += " -> "
            current_node = current_node.next
        print(string)

    def queue_size(self) -> int:
        current_node = self.head
        size = 0
        while current_node:
            current_node = current_node.next
            size += 1
        return size