from collections import deque
import sys

n, k = map(int,sys.stdin.readline().split())
q = deque([i for i in range(1, int(n)+1)])

answer = []

while q:
    for _ in range(k):
        x = q.popleft()
        q.append(x)
    answer.append(q.pop())

print("<" + ', '.join(map(str,answer)) + ">")
