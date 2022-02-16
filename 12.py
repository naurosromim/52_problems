n = 100

f = 1

while n>=1:
    f = f*n
    n = n-1

f = str(f)


l = len(f)-1

c = 0

while l>=0:
    if f[l] == '0':
        c = c+1
    else:
        break
    l = l-1


print(c)