n, m = map(int, input().split())

answer = 0
for i in range(n):
    row = list(map(int, input().split()))
    # 각 행에서 가장 작은 수 찾기
    min_value = min(row)
    # 뽑은 수 중에서 큰 수를 answer에 저장
    answer = max(answer, min_value)

print(answer)
