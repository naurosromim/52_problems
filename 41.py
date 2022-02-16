T = int(input())

def factorial(k):
    g = 1
    for i in range(k):
        g = g*(i+1)
    return g


for t in range(T):
    n = int(input())
    r = 0

    while n>=1:
        f = factorial(n)
        r = r + n/f
        n = n-1
    print(r)
