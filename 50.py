T = int(input())

for t in range(T):
    number = input()

    number = [n for n in number]
    l = len(number)

    for i in range(l):
        if number[i] == 'L':
            number[i] = number[i-1]
        elif number[i] == 'R':
            number[i] = number[i+1]
    
    number = ''.join(number)

    print(number)