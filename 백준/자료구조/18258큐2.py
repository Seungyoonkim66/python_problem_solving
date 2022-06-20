from collections import deque
import sys


n = int(sys.stdin.readline())
q = deque([])
for _ in range(n):
    command = sys.stdin.readline().split()
    c = command[0]
    if c == "push":
        q.append(command[1])
    elif c == "pop":
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif c == "size":
        print(len(q))
    elif c == "empty":
        if not q:
            print(1)
        else:
            print(0)
    elif c == "front":
        if not q:
            print(-1)
        else:
            print(q[0])
    elif c == "back":
        if not q:
            print(-1)
        else:
            print(q[-1])