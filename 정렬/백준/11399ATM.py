n = int(input())
times= list(map(int, input().split()))
# times = [3, 1, 4, 3, 2]
times.sort()
total = 0

for i in range(len(times)):
    total += sum(times[0:i+1])

print(total)