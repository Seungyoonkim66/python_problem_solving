import sys

def solution(s, length):
    answer = 0
    print(s, length)
    
    return answer

s = sys.stdin.readline().rstrip()
result = []
for i in range(1, len(s)+1):
    result.append(solution(s, i)) 