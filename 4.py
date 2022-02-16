t = int(input())

for i in range(1,t+1):
    n = int(input())

    k = 1
    m = []

    while k<=n:
        if n%k==0:
            m.append(str(k))
        k = k+1

    result = 'Case ' + str(i) + ' : ' + ' '.join(m)

    print(result)

