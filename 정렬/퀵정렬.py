array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array:list, start:int, end:int):
    if start >= end: # 원소가 1개인 경우 재귀 종료
        return
    
    pivot = start # 피벗은 첫번째 요소 
    left = start + 1 # 피벗 바로 오른쪽 요소부터 시작 
    right = end 

    while left <= right: # 왼쪽 포인터와 오른쪽 포인터가 교차되지 않을 때까지 반복 
        # left가 배열 내에서 왼->오 방향으로 탐색하면서 피벗보다 큰 값을 발견할 때까지 이동 
        while left <= end and array[left] <= array[pivot]:
            left += 1
        
        # right가 배열 내에서 오->왼 방향으로 탐색하면서 피벗보다 작은 값을 발견할 때까지 이동 
        while right > start and array[right] >= array[pivot]:
            right -= 1

        # left, right 각각 탐색하다가 서로 얼갈린 경우 피벗과 작은 데이터를 swap 
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않고 그냥 left가 피벗보다 큰 값이고 right가 피벗보다 작은 값인 것을 swap 
        else:
            array[left], array[right] = array[right], array[left]
    
    quick_sort(array, start, right-1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array)-1)
print(array)