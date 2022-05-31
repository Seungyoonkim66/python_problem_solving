n = 6
m = 10
k = 3
# => 3

n,m,k = map(int, input().split())
team = 0
while True:
    n -= 2
    m -= 1
    # 여학생 또는 남학생 수가 부족하거나 전체 학생 중에 인턴 갈 사람이 없다면 팀 생성 X
    if (n < 0 or m < 0 or (n+m) < k):
        break
    team+=1
print(team)