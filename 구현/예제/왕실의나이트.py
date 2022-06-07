def checkRange(nums) -> bool:
    result = True
    for num in nums:
        if 0 >= num or num > 8:
            return False
    return result

def night(loc):
    c = ord(loc[0])-96
    r = int(loc[1])

    cnt = 0   
    if checkRange([c-2, r+1]) :
        cnt+=1 
    if checkRange([c-2, r-1]):
        cnt+=1

    if checkRange([c+2, r+1]):
        cnt+=1
    if checkRange([c+2, r-1]):
        cnt+=1
    
    if checkRange([c+1, r+2]):
        cnt+=1
    if checkRange([c-1, r+2]):
        cnt+=1
    
    if checkRange([c+1, r-2]):
        cnt+=1
    if checkRange([c-1, r-2]):
        cnt+=1

    return cnt

if __name__ == "__main__":
    loc = input()
    # loc = "a1" # => 2
    print(night(loc))