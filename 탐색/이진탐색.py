def binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start +  end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target: # 중간점 왼쪽 확인
        return binary_search(array, target, start, mid-1)
    else: # 중간점 오른쪽 확인
        return binary_search(array, target, mid + 1, end)