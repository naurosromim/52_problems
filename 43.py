T = int(input())
for t in range(T):
    p,q,c = input().split()
    p = int(p)
    q = int(q)
    c = int(c)

    ans = 1
    for i in range(q):
        ans = ans*p
    
    print(ans%c)