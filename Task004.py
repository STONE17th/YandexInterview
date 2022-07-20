import random

def create_random_array(list: list):
    for i in range(len(list)):
        list[i] = random.randint(0,1)
    return list

def lenght_list(list: list):
    for i in range(len(list)-1, -1, -1):
        if list[i] == 1:
            return i

def list_without_zero (list: list, index: int):
    new_list = list[:]
    new_list.append(0)
    new_list.append(0)
    for i in range(index, len(list)):
        if new_list[i] == 1 and new_list[i + 1] == 0 and new_list[i + 2] == 1:
            new_list.pop(i + 1)
            new_list.pop(len(new_list)-1)
            return new_list, i + 1

def check_interval(list: list):
    max_count = []
    for element in list:
        new_string = ""
        example_string = 1
        for char in element:
            new_string += str(char)
        while True:
            if str(example_string) in new_string:
                example_string = str(example_string) + "1"
            else:
                max_count.append(len(str(example_string))-1)
                break
    return max_count

bi_list = [0] * 20
new_bi_list = [bi_list]
index = 0
max_list = []

print(create_random_array(bi_list))

while (index<lenght_list(bi_list)):
    if list_without_zero(bi_list, index) != None:
        new_bi_list.append(list_without_zero(bi_list, index)[0])
        index = list_without_zero(bi_list, index)[1]
        index += 1
    else:
        break

print(f"Максимальный интервал из едениц в бинарном списке:  {max(check_interval(new_bi_list))}")