import re
total = 0
AmountOfNumbers = 0
file = open(r'TestData/mbox.txt')
for line in file:
  match = re.findall(r'New Revision: (\d+)', line)
  if len(match) > 0: 
    total = total + int(match[0])
    AmountOfNumbers += 1

print(int(total/AmountOfNumbers))
file.close()