import sys

n = int(sys.stdin.readline().rstrip())
# n = 3 
d = [0] * 1001
d[1] = 2
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] + d[1-2]*2) % 796796
print(d[n])
