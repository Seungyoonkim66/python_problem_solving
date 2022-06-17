from torch import le


def selection_sort(array:list) -> list:
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
            array[i], array[min_idx] = array[min_idx], array[i]
    print(array)
    return array

def insertion_sort(array:list) -> list:
    if len(array) < 2 :
        print(array)
        return 

    for i in range(1, len(array)): # 두번째 요소부터 시작 
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break

    print(array)
    return array


def quick_sort(array:list, start:int, end:int) -> list:
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end 

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    
    quick_sort(array, start, right-1)
    quick_sort(array, right + 1, end)

    return array

def quick_sort_2():
    pass

def count_sort(array:list) -> list:
    max_num = max(array)
    cnt = [0 for i in range(max_num+1)]
    print(cnt)
    for i in array:
        cnt[i] += 1
    print(cnt)

    for j in range(len(cnt)):
        for _ in range(cnt[j]):
            print(j, end=' ')
    return array
    
p

array = [7,5,9,0,3,1,6,2,4,8]
# selection_sort(array)
# insertion_sort(array)
# print(quick_sort(array, 0, len(array)-1))
# count_sort(array)