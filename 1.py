t = int(input())

for i in range(t):
    n = int(input())
    if n>100:
        break

    if n%2==0:
        print('even')
    else:
        print('odd')