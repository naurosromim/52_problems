t = int(input())

for f in range(1,t+1):
    n = input().split()

    for i in range(len(n)):
        for j in range(len(n)-1):
            if n[j] > n[j+1]:
                temp = n[j]
                n[j] = n[j+1]
                n[j+1] = temp
    
    n = ' '.join(n)
    result = 'Case ' + str(f) + ': ' + n
    print(result)