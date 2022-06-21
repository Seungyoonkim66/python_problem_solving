def seqential_search(array:list, target:str) -> bool:
    for e in array:
        if e == target:
            return True
    return False

array = ['Hanul', 'Jonggu', 'Dongbin', 'Taeil' , 'Sangwook']
print(seqential_search(array, 'Dongbin'))