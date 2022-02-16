a,b = input().split()
a = int(a)
b = int(b)

def divide(x):
    n = 2
    while True:
        if x%n == 0:
            return x/n, n
            break
        n = n+1

def return_2(x):
    factor = []
    while True:
        if x == 1:
            break
        x, n = divide(x)
        factor.append(n)
    return factor

factor_a = return_2(a)
factor_b = return_2(b)

#print(factor_a)
#print(factor_b)

if len(factor_b) > len(factor_a):
    temp = factor_a
    factor_a = factor_b
    factor_b = temp

#print(factor_a)
#print(factor_b)

for i in factor_b:
    if i not in factor_a:
        factor_a.append(i)

ans = 1

for i in factor_a:
    ans = ans*i

print(ans)