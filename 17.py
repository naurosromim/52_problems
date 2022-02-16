sen = 'i am a programmer'

sen = sen.split()
sen = ''.join(sen)

vowels = ['a','e','i','o','u']

count = 0

for c in sen:
    if c in vowels:
        count = count+1

result = 'Number of vowels = ' + str(count)

print(result)