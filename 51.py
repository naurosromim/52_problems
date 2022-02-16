t = int(input())

for f in range(t):
    string, sub_string = input().split()

    l_string = len(string)
    l_substring = len(sub_string)

    for i in range(l_string):
        k = 0

        for j in range(l_substring):
            if string[i+j] == sub_string[j]:
                k = k+1
            else: break
        
        if k == l_substring:
            break
    
    print(i)