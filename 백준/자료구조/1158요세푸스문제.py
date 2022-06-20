from collections import deque
import sys

# n, k = sys.stdin.readline().split()
n = 7
k = 3
q = deque([i for i in range(1, int(n)+1)])
while q:
    print(q[k])
    del q[k]
# print(q)
