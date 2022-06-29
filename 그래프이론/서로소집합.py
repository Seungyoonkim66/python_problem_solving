# def find_parent(parent_table, x):
#     if parent_table[x] != x: # 현재 노드와 부모 노드가 다르면 루트 노드가 아니라는 의미니까 거슬러 올라가기 
#         return find_parent(parent_table, parent_table[x])
#     return x
def find_parent(parent_table, x): # 경로 압축 기법 사용 
    if parent_table[x] != x:
        parent_table[x] = find_parent(parent_table, parent_table[x])
    return parent_table[x]

def union_parent(parent_table, a, b):
    a = find_parent(parent_table, a)
    b = find_parent(parent_table, b)

    if a < b:
        parent_table[b] = a
    else:
        parent_table[a] = b
    
v, e = map(int, input().split())
parent_table = [0] * (v+1)
for i in range(1, v+1):
    parent_table[i] = i # 처음엔 자기 자신을 부모 노드로 초기화 

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent_table, a, b)

print('각 원소가 속한 집합: ', end="")
for i in range(1, v+1):
    print(find_parent(parent_table, i), end=" ") # 루트 노드가 같은 것끼리 같은 집합임을 의미 
print()
print("부모 테이블: ", end="")
for i in range(1, v+1):
    print(parent_table[i], end=' ')
