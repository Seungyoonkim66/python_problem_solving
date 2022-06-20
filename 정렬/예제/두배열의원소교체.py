n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# n = 5
# k = 3
# A, B = [1, 2, 5, 4, 3], [5, 5, 6, 6, 5]
A.sort()
B.sort(reverse=True)

for i in range(k):
    A[i], B[i] = B[i], A[i]

print(sum(A))