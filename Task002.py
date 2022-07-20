orig_string = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'
counter = 0
new_string = ''
prev_char = 'A'
for index in range(len(orig_string)):
    if orig_string[index] != prev_char:
        if counter == 1:
            new_string += prev_char
        else:
            new_string += prev_char + str(counter)
            counter = 1
    else:
        counter += 1
    prev_char = orig_string[index]
    if index == len(orig_string) - 1:
        new_string += prev_char + str(counter)

print(new_string)