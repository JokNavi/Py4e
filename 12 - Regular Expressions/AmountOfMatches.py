import re
x = list()
pattern = input("Enter a regular expression: ")
file = open(r'TestData/mbox.txt')
for line in file:
    x.extend(re.findall(pattern, line))
print(len(x))