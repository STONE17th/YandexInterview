import numpy as np

def print_matrix(list: list):
    for row in range(len(list)):
        for string in range(len(list)):
            print(list[row][string], sep = " | ", end = " ")
        print()

def create_clean_matrix(list: list):
    max_day = 0
    max_guest = 0
    for guest in list:
        if guest[1] > max_day: max_day = guest[1]
        max_guest += 1
    new_booking = np.zeros((max_day,max_guest))
    return new_booking

def busy_list(list: list):
    day = 0
    for guest in list:
        for i in range(guest[0]-1,guest[1]):
            new_booking[i][day] = 1
        day += 1
    return new_booking

def max_guest_day(list: list):
    summ_list = []
    day = 1
    for i in list:
        summ = i.sum()
        summ_list.append([summ, day])
        day += 1
    maxg = 0
    maxd = None
    for max_guest in summ_list:
        if max_guest[0] > maxg:
            maxg = max_guest[0]
            maxd = max_guest
    return maxd[1]

guest_list = [ (1, 2), (1, 3), (3, 4), (3, 4), (2,5), (4,5), (3,5), (2,5), (4,5)]

print(f"Даты прибывания гостей {guest_list}")
new_booking = create_clean_matrix(guest_list)
new_booking = busy_list(guest_list)

print(f"Максимально постояльцев одновременно было в {max_guest_day(new_booking)} день")

