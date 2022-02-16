T = int(input())
for t in range(T):
    x,k = input().split()
    x = int(x)
    k = int(k)

    r = 1

    for i in range(1,k+1):
        f=1
        for j in range(i):
            f = f*x
        r = r + f
    print(r)