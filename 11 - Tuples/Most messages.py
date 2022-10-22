words = dict()
items = list()
with open('mbox-short.txt') as f:
    for line in f.readlines():
        if line.startswith('From') and not line.startswith('From:'):
            sender = line.split()[1]
            if sender not in words:
                words.update({sender: 1}) 
            else:
                words.update({sender: words[sender]+1}) 

for key, value in words.items():
    items.append((value, key))

items.sort(reverse=True)
value, key = max(items)
print(f"{key} {value}")