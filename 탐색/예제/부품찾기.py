import sys

n = int(sys.stdin.readline().rstrip())
parts = list(map(int, sys.stdin.readline().rstrip()))
parts.sort()
m = int(sys.stdin.readline().rstrip())
order = list(map(int, sys.stdin.readline().rstrip()))


def binary_search(array:list, left:int, right:int, target:int):
    while left <= right:
        mid = (left + right) // 2

        if(array[mid] == target):
            return mid
        elif array[mid] < target: # 타겟이 더 크면 오른쪽 트리 탐색 (mid + 1) ~ right 
            left = mid + 1
        elif array[mid] > target: # 타겟이 더 작으면 왼쪽 트리 탐색 lefgt ~ (mid - 1) 
            right = mid - 1
    return None

for part in order:
    result = binary_search(parts, part, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

