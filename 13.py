t = int(input())

for f in range(t):

    sen = input().split()

    d = {}

    for w in sen:
        if w not in d.keys():
            d[w] = 1
        else:
            d[w] = d[w] + 1
    
    n = len(sen)

    factorial = 1

    while n>0:
        factorial = factorial * n
        n = n - 1
    

    for i in d.values():
        factorial = factorial/i
    
    print(int(factorial))
