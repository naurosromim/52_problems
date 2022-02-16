sen = input().split()
sen2 = []

for w in sen:

    l = len(w)
    half = int(l/2)

    w = [i for i in w]
    print(w)

    for i in range(half):
        temp = w[i]
        w[i] = w[l-1-i]
        w[l-1-i] = temp
    
    w = ''.join(w)
    sen2.append(w)
    
sen = ' '.join(sen2)

print(sen)