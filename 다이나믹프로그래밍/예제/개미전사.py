import sys


n = int(sys.stdin.readline().rstrip())
warehouses = list(map(int, sys.stdin.readline().rstrip().split()))

# n = 4
# warehouses = [1, 3, 1, 5]
d = [0]*101 
d[0] = warehouses[0]
d[1] = max(warehouses[0], warehouses[1])

for i in range(2,n):
    # d[i-1] : 현재 창고 옆 창고 털기 
    # d[i-2] + warehouses[i] : 현재 창고 + 옆옆 창고 털기 
    # d[i] = 그 중에 큰 값을 저장 
    d[i] = max(d[i-1], d[i-2] + warehouses[i])

    # print(i)
    # print('d[i-1] : ', d[i-1])
    # print('d[i-2] + warehouses[i]: ', d[i-2] + warehouses[i])
    # print('d[i] : ', d[i])


print(d[n-1])