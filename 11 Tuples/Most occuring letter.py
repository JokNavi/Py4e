alphabet_s = "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z".replace(" ", "")
alphabet = [letter for letter in alphabet_s.lower().split(",")]

letters = dict()
with open('mbox-short.txt') as f:
    for line in f.readlines():
        characters = list(line.lower())
        for char in characters:
            if char in alphabet and char not in letters:
                letters.update({char: 1})
            elif char in alphabet:
                letters.update({char: letters[char]+1})

lst = list()
for key, value in letters.items():
    lst.append((value, key))

lst.sort(reverse=True)
for value, key in lst:
    print(key, value)
