import re
x = list()
file = open(r'TestData/mbox.txt')
for line in file:
    x.extend(re.findall(r'New Revision: \d+\.?\d+', line))
print(len(x))
file.close()