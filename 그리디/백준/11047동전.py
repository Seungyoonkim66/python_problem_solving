# n = 10 
# k = 1200
# coins = [1,5,10,50,100,500,1000,5000,10000,50000]
# => 12

n,k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
# 오름차순으로 입력하니까 내림차순으로 정렬해주기 
coins.reverse()
answer = 0
for coin in coins: 
    cnt = k//coin
    answer += cnt
    k = k - cnt*coin

print(answer)