def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))


d = [0] * 100 # memoization에 활용할 리스트 초기화 
def fibo_memo(x):
    if x == 1 or x == 2:
        return 1
    
    if d[x] != 0: # 계산한 이력이 있다면
            return d[x]
    
    d[x] = fibo_memo(x-1)  + fibo_memo(x-2)
    return d[x]

print(fibo_memo(99))

def fibo_loop(x):
    d = [0] * 100
    d[1] = 1
    d[2] = 1
    n = 99

    for i in range(2, n+1):
        d[i] = d[i-1] + d[i-2]
    
    return d[n]
    
print(fibo_loop(99))

