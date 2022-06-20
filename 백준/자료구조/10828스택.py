import sys
n = int(sys.stdin.readline())
s = []

for _ in range(n):
    command = sys.stdin.readline().split()
    c = command[0]

    if c == "push":
        s.append(command[1])
    elif c == "pop":
        if len(s) == 0:
            print(-1)
        else:
            print(s.pop())
    elif c == "size":
        print(len(s))
    elif c == "top":
        if len(s) == 0:
            print(-1)
        else:
            print(s[-1])
    elif c == "empty":
        if len(s) == 0:
            print(1)
        else:
            print(0)


# class Node:
#     def __init__(self, data) -> None:
#         self.data = data
#         self.next = None

# class Stack:
#     def __init__(self) -> None:
#         self.top = None
#         self.size = 0

#     def empty(self) -> int:
#         if self.top == None:
#             return 1
#         else:
#             return 0
    
#     def push(self, data:int) -> None:
#         new_node = Node(data)
#         if self.top != None:
#             new_node.next = self.top
#         self.top = new_node
#         self.size += 1
    
#     def pop(self) -> int:
#         if self.top == None:
#             return -1
#         else:
#             popped = self.top.data
#             self.top = self.top.next
#             self.size -= 1
#             return popped

#     def get_top(self) -> int:
#         if self.top == None:
#             return -1
#         return self.top.data

# n = int(sys.stdin.readline())
# s = Stack()

# for _ in range(n):
#     command = input().split()
#     c = command[0]

#     if c == "push": 
#         s.push(int(command[1]))
#     elif c == "pop":
#         print(s.pop())
#     elif c == "size":
#         print(s.size)
#     elif c == "empty":
#         print(s.empty())
#     elif c == "top":
#         print(s.get_top())


