T = int(input())
for t in range(T):
    array = []
    x = int(input())
    for i in range(x):
        a = int(input())
        array.append(a)
    
    result_ascending = 'YES'
    result_descending = 'YES'

    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            result_ascending = 'NO'
            break
    for i in range(len(array)-1):
        if array[i] < array[i+1]:
            result_descending = 'NO'
    if result_ascending == 'NO' and result_descending == 'NO':
        print('NO')
    else:
        print('YES')
