T = int(input())
for t in range(T):
    n = input()
    if ord(n) >=97 and ord(n) <=122:
        print('Lowercase character')
    elif ord(n) >= 65 and ord(n) <= 90:
        print('Uppercase character')
    elif ord(n) >= 48 and ord(n) <= 57:
        print('Numerical digit')
    else:
        print('Special character')