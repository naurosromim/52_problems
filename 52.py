t = int(input())

for f in range(t):
    string, substring = input().split()
    l_string = len(string)
    l_substring = len(substring)

    c = 0

    for i in range(l_string-l_substring+1):
        k = 0
        for j in range(l_substring):
            if string[i+j] == substring[j]:
                k = k+1
            else: break
        if k == l_substring:
            c = c+1
    print(c)