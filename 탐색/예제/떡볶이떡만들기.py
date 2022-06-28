import sys


ddeok, order_ddeok_len = map(int, sys.stdin.readline().rstrip().split())
ddeoks = list(map(int, sys.stdin.readline().rstrip().split()))

# 이진 탐색 시작 위치와 종료 위치 초기화
start = 0
end = max(ddeoks)

# 절단기의 높이
result = 0

while (start < end):

    # 절단기 높이 지정
    cut_height = (start+end)//2

    left_ddeok_len = 0
    # 절단기로 모든 떡을 잘랐을 때, 남은 떡의 길이 계산
    for ddeok in ddeoks:
        # 떡의 높이가 더 높을 때만 자를 수 있음
        if (ddeok > cut_height):
            left_ddeok_len += ddeok - cut_height

    # 남은 떡의 길이가 손님이 요청한 떡의 길이보다 적을 경우, 
    # 절단기의 높이를 낮춰야함
    if (left_ddeok_len < order_ddeok_len):
        end = cut_height - 1

    # 남은 떡의 길이가 손님이 요청한 떡의 길이보다 많거나 같을 경우, 
    # 해당 절단기의 높이를 기록하고, 절단기의 높이를 높여야함
    else:
        result = cut_height
        start = cut_height + 1

print(result)
