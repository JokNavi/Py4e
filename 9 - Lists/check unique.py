words = list()
unique = list()

with open('romeo.txt') as f:
    for line in f:
        words.extend(line.split())

for item in words:
    if item not in unique:
        unique.append(item)

print(words)
print(unique)