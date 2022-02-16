T = int(input())
#N = input().split()
a = [int(i) for i in input().split()]

for n in a:

    def perfect_number(x):
        y = x - 1
        factors = 0
        while y>=1:
            if x%y == 0:
                factors = factors + y
            y = y-1
        if factors == x:
            return True
        else:
            return False
        
    pn = []

    for i in range(1,n+1):
        if perfect_number(i):
            pn.append(i)
    for i in pn:
        print(i)


