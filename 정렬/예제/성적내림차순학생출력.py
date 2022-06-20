n = int(input())
students = [tuple(input().split()) for _ in range(n)]
# students = [('홍길동', '95'), ('이순신', '77')]

students.sort(key=lambda x: x[1])
for student in students:
    print(student[0], end=" ")