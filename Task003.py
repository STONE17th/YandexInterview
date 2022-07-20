def sort_list(orig_list: list):
    reserve = 0
    for i in range(len(orig_list)):
        for j in range(len(orig_list) - 1):
            if orig_list[j] > orig_list[j+1]:
                orig_list[j], orig_list[j+1] = orig_list[j+1], orig_list[j]
    return orig_list

def check_interval(orig_list: list):
    count = 0
    orig_list.append(None)
    new_list = []
    for i in range(len(orig_list)-1):
        if orig_list[i] + 1 != orig_list[i + 1] or i == len(orig_list) - 1:
            if count == 0:
                new_list.append(orig_list[i])
            else:
                new_list.append(f"{orig_list[i] - count}-{orig_list[i]}")
                count = 0
        else:
            count += 1
    return new_list


a_list = [1,4,5,2,3,9,8,11,0]
b_list = [1,4,3,2]
c_list = [1,4]


print(*check_interval(sort_list(a_list)))
print(*check_interval(sort_list(b_list)))
print(*check_interval(sort_list(c_list)))