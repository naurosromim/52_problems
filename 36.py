t = int(input())
word = []
for i in range(t):
    a = input()
    word.append(a)

for i in range(len(word)-1):
    for j in range(len(word)-1):
        if ord(word[j][0]) > ord(word[j+1][0]):
            temp = word[j]
            word[j] = word[j+1]
            word[j+1] = temp

for i in word:
    print(i)
