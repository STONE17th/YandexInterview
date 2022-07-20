def group_words(words: list[str]) -> list[list[str]]:
    group_keys = []
    for word in words:
        group_keys.append(''.join(sorted(word)))

    group_keys = sorted(set(group_keys))
    group_words = [[],[],[]]

    i = 0

    for group in group_keys:
        for word in words:
            if "".join(sorted(word)) == group:
                group_words[i].append(word)
        i += 1

    print(group_words)

list_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(list_words)

group_words(list_words)