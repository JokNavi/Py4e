words = dict()
max_value = 0
max_item = ""
with open('mbox-short.txt') as f:
    for line in f.readlines():
        if line.startswith('From') and not line.startswith('From:'):
            sender = line.split()[1]
            if sender not in words:
                words.update({sender: 1}) 
            else:
                words.update({sender: words[sender]+1}) 

for key in words:
    if words.get(key) > max_value:
        max_value = words.get(key)
        max_item = key

print(f'{max_item} {max_value}')