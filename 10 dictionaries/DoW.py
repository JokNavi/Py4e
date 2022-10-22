words = dict()
with open('mbox-short.txt') as f:
    for line in f.readlines():
        if line.startswith('From') and not line.startswith('From:'):
            day = line.split()[2]
            if day not in words:
                words.update({day: 1}) 
            else:
                words.update({day: words[day]+1}) 
print(words)