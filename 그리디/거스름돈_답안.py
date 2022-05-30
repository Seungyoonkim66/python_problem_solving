N = 1260
answer = 0
coins = [500, 100, 50, 10]
for coin in coins:
    answer += N//coin
    N %= coin

print(answer)

# 입력값이 아닌 문제에 주어진 조건, 즉 동전의 종류 개수에만 영향을 받는 알고리즘으로 작성해야 한다. 
