T = int(input())
for t in range(T):
    n = int(input())

    result = ''

    while n>=0:
        if n ==0:
            r = '1'
            result = result+r
        elif n==1:
            r = '2' + ' + '
            result = result+r
        else:
            r = '2^'+str(n)+' + '
            result = result + r
        n = n-1
    print(result)
