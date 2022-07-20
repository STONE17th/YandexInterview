a_list = [1, 2, 2, 3]
b_list = [5, 1, 2, 7, 3, 2]
new_list = []
for element in a_list:
    for elem in b_list:
        if element == elem:
            new_list.append(element)
            break
print(*new_list)