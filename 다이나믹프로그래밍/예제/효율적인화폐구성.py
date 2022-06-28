import sys

# dp 배열의 index는 가치, value는 화폐 개수이다. 처음에는 value를 무한대 값으로 초기화한다. 
# 단 가치 0원을 만들기 위해 필요한 화폐 개수는 0개이므로 dp[0] = 0이다.
# 가치 1원부터 가치 M원까지 탐색하며, 한 번 탐색할 때마다 모든 화폐를 탐색한다. (이중반복문)

n, m = map(int, sys.stdin.readline().rstrip().split())
coins = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

d = [float('inf')] * (m+1)
d[0] = 0 

# 1부터 구해야하는 가치까지 모든 값을 탐색 
for i in range(1, m+1):
    for coin in coins: # 각 값마다 모든 화폐 종류 탐색
        if i >= coin: # 화폐가 구해야 하는 가치보다는 작아야한다. 
            d[i] = min(d[i], d[i-coin] + 1) # 이 점화식을 어떻게 구하니

if d[m] == float('inf'):
    print(-1)
else:
    print(d[m])