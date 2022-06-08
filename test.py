from itertools import product

def maxEnergy(mat:list)->int:
    energy = 100
    cand = [[(i,j) for j in range(len(mat[0]))] for i in range(len(mat))]
		# [[(0,0),(0,1),(0,2),(0,3)],[(1,0),(1,1),(1,2),(1,3)],[(2,0),(2,1),(2,2),(2,3)],[(3,0),(3,1),(3,2),(3,3)]]
    possible_cands = list(product(*cand))
		# 4 X 4 X 4 X 4 
    # print(cand)
    # print(len(possible_cands))
    # print(possible_cands)



    filt=[]
    for path in possible_cands: 
        flag=True
        previous_row=[]
        for row in path:
            if previous_row:    
                if abs(previous_row[-1][1] - row[1])>1:
                    flag=False
                    break 
            previous_row.append(row)
            
        if flag:
            filt.append(path)
    
    min_sum_nums=energy
    for path in filt:
        sum_nums = sum([mat[i][j] for i,j in path])
        min_sum_nums = min(min_sum_nums,sum_nums)

    return energy-min_sum_nums


mat = [
    [4,6,14,21],
    [17,0,5,5],
    [4,41,22,3],
    [2,51,6,0]
]
maxEnergy(mat)