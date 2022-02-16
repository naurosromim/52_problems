sen = 'i am a programmer'

sen = [i for i in sen]

count = 0

for i in sen:
    if i == ' ':
        count = count +1

print(count)