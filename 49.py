T = int(input())

for t in range(T):
    n = int(input())

    result = ' is a prime'

    if n==2:
        result = ' is a prime'
    elif n%2 == 0:
        result = ' is not a prime'
    else:
        k = 3
        while True:
            if n%3 == 0:
                result = ' is not a prime'
                break
            k = k+2
            if k>= n:
                break
    
    print(str(n) + result)