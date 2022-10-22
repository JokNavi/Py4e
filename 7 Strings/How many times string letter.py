def counting(word, character):
    count = 0
    for letter in word:
        if letter == character:
            count = count + 1
    return count

print(counting('banana', 'a'))
print(counting('testing you because you\'re cute', 'a'))