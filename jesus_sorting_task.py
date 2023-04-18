list = [6, 2, 7, -3, 4, 8, 9, -8, 0, 2, 5]

for i in range(0, len(list)):
    smallest_index = i
    for n in range(i, len(list)):
        if list[n] < list[smallest_index]:
            smallest_index = n
    
    copy = list[i]
    list[i] = list[smallest_index]
    list[smallest_index] = copy

print(list)