T = int(input())

for t in range(T):
    N = input()

    n = [int(i) for i in N]

    def cube(x,y):
        ans = 1
        l = len(y)
        for i in range(l):
            ans = ans*x
        return ans

    ans = 0

    for i in n:
        c = cube(i,N)
        ans = ans + c
    


    if ans == int(N):
        print('armstrong number')
    else:
        print('not armstrong number')

    