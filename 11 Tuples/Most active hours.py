most_active_hours = dict()
lst = list()
with open('mbox-short.txt') as f:
    for line in f.readlines():
        if line.startswith('From') and not line.startswith('From:'):
            time = line.split()[5]
            current_time = time.split(":")[0]
            if current_time not in most_active_hours:
                most_active_hours.update({current_time: 1})
            else:
                most_active_hours.update({current_time: most_active_hours[current_time]+1})


for key, value in most_active_hours.items():
    lst.append((key, value))


lst.sort()
for key, value in lst:
    print(key, value)

