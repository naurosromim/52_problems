T = int(input())
for t in range(T):
    s = input()
    s = [i for i in s]

    L = len(s)
    l = int(L/2)
    result = 'YES'

    for i in range(l):
        if s[i] != s[L-1-i]:
            result = 'NO'
    print(result)