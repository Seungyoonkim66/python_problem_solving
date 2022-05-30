answer = 0
N = int(input("거슬러 줘야 할 돈은 얼마인가요?"))
# N = 1260
while(N != 0) :
    if(N >= 500):
        N = N - 500
    elif(N >= 100):
        N = N -100
    elif(N >= 50):
        N = N - 50
    elif(N >= 10):
        N = N - 10 
    answer+=1

print(answer)

# 복잡도가 N의 크기에 따라 달라지기 때문에 거슬러 줘야할 금액이 커질수록 불리한 알고리즘 