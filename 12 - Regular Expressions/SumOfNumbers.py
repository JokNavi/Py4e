import re
print(sum([int(i) for i in re.findall(r'[0-9]+', open(r'RawTextFiles/regex_sum_1664978.txt').read())]))