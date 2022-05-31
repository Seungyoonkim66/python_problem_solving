# example 
# n = 25 
# k = 5
# output = 2
n, k = map(int, input().split())

answer = 0
while True:
    # 1이 되면 탈출
    if n == 1:
        break

    # 연산 수행할 때마다 1씩 더하기 
    answer +=1 

    # n이 k의 배수면 우선 2번. 나눗셈을 해주고 while 문 다시 돌기
    if n%k == 0:
        n = n//k
        continue
    # 그렇지 않은 경우 1번. 뺄셈 해주기 
    n -= 1
    
print(answer)