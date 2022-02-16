#n, m = input().split()
#n = int(n)
#m = int(m)
#n = 2*n-1

n = 5
m = 2

hp = int(n/2) + 1

numbers = []

for i in range(1,hp):
    numbers.append(i)

numbers.append(hp)

a = int(n/2)
while a>=1:
    numbers.append(a)
    a = a-1

for i in numbers:
    for j in range(i):
        print(m, end=' ')
    print('')