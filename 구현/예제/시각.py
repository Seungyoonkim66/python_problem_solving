def timeIncludes3(n):
    cnt=0
    for h in range(n+1):
        for m in range(60):
            for s in range(60):
                if '3' in (str(h) + str(m) + str(s)):
                    cnt += 1

    return cnt


if __name__ == "__main__":
    # n = int(input())
    n = 5 # -> 11475
    print(timeIncludes3(n))
