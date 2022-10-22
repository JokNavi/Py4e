fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(line) < 2 or words[0] != 'From' : continue
    print(words[2])