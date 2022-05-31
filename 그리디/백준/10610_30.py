# n = 80875542 # 88755420
# n = 2931 # -1
# n = 102 # 210

n = list(input())
# 가장 큰 값을 구하려면 내림차순으로 만들어야 됨 
n.sort(reverse=True)
sum = 0

if "0" not in n:
    print(-1)
else :
    for i in n:
        sum += int(i)
    if sum%3 != 0:
        print(-1)
    else:
        print(''.join(n))

