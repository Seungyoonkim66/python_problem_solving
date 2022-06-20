import sys

def check_ps(ps:str) -> None:
    s = []
    psl = list(ps)

    for p in psl:
        if p == "(":
            s.append("(")
        elif p == ")":
            if len(s) == 0 :
                print("NO")
                return
            s.pop()
    
    if len(s) == 0:
        print("YES")
    else:
        print("NO")


n = int(input())
for _ in range(n):
    ps = sys.stdin.readline().strip()
    check_ps(ps)

