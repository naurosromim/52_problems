t = int(input())

for f in range(t):
    sen_org = input()
    sen = sen_org.split()
    sen = ''.join(sen)

    d = {}

    for c in sen:
        if c not in d.keys():
            d[c] = 1
        else:
            d[c] = d[c]+1
    
    find = input()

    if find not in d.keys():
        result = "'" + find + "' is not present"
        print(result)
    else:
        result = "Occurance of '" + find + "' in " + sen_org + ' = ' + str(d[find])
        print(result)