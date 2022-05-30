# N, M, K = input().split()
# arr = list(map(int, input().split()))

answer = 0
N = 5
M = 8 
K = 3
arr = [2,4,5,4,6]
arr.sort()
first = arr.pop(-1)
second = arr.pop(-1)
# first가 K번 + second 1번 이걸 반복하면 됨 s
# 반복되는 수열의 길이 = K + 1
# first * 3 , second * 1 수열이 반복되는 횟수 = M // (K+1)
# first가 더해지는 횟수 
cnt = (M//(K+1) * K) + (M % (K+1))
answer += first * cnt + second * (M-cnt)
print(answer)





