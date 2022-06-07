def udrl(n, directions):
    loc = (1,1)
    for d in directions:
        if d == "R":
            if loc[1] == n:
                continue
            loc = (loc[0], loc[1]+1)
        elif d == "L":
            if loc[1] == 1:
                continue
            loc = (loc[0], loc[1]-1)
        elif d == "U":
            if loc[0] == 1:
                continue
            loc = (loc[0]-1, loc[1])
        elif d == "D":
            if loc[0] == n:
                continue
            loc = (loc[0]+1, loc[1])

    return ' '.join([str(l) for l in loc])

if __name__ == "__main__":
    n = int(input())
    directions = list(input().split(" "))
    # n = 5
    # directions = ['R','R','R','U','D','D']
    print(udrl(n, directions))
