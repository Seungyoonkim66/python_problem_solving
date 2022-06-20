from collections import deque
import sys

n = int(sys.stdin.readline().strip())
q = deque([])
for _ in range(n):
    command = sys.stdin.readline().split()
    c = command[0]
    if c == "push_front":
        q.appendleft(command[1])
    if c == "push_back":
        q.append(command[1])
    if c == "pop_front":
        if not q:
            print(-1)
        else:
            print(q.popleft())
    if c == "pop_back":
        if not q:
            print(-1)
        else:
            print(q.pop())
    if c == "size":
        print(len(q))
    if c == "empty":
        if q :
            print(0)
        else:
            print(1)
    if c == "front":
        if not q:
            print(-1)
        else:
            print(q[0])
    if c == "back":
        if not q:
            print(-1)
        else:
            print(q[len(q)-1])