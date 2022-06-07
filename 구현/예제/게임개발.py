from multiprocessing.dummy import current_process

from regex import P


def developGame(board_size, loc, board):
    n = board_size[0]
    m = board_size[1]
    x = loc[0]
    y = loc[1]
    d = loc[2]

    visited = []
    xys = []
    left = (x-1, y)
    right = (x+1, y)
    up = (x, y+1)
    down = (x, y-1)

    if d==0:
        xys = [left, down, right, up]
    elif d==1:
        xys = [down, right, up, left]
    elif d==2:
        xys = [right, up, left, down]
    elif d==3:
        xys = [up, left, down, right]

    print(board)
    print(xys)
    for xy in xys:
        print(board[xy[1]][xy[0]])
    



    return

if __name__ == "__main__":
    # n, m = map(int, input().split(' '))
    # x, y, d = map(int, input().split(' '))
    # board = [list(map(int, input().split(" "))) for i in range(m)]

    n = 4
    m = 4
    x = 1
    y = 1
    d = 0 
    board = [
        [1,1,1,1],
        [1,0,0,1],
        [1,1,0,1],
        [1,1,1,1]
    ] # => 3

    print(developGame((n,m), (x,y,d), board))