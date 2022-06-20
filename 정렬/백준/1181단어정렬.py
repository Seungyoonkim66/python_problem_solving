n = int(input())
words = [input() for _ in range(n)]
# words = ['but', 'i', 'wont', 'hesitate', 'no', 'more', 'no', 'more', 'it', 'cannot', 'wait', 'im', 'yours']
printed = []
words.sort(key=lambda x: (len(x), x))
for word in words:
    if word in printed: 
        continue
    printed.append(word)
    print(word)
    

    