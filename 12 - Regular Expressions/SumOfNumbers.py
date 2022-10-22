import re
print(sum([int(i) for i in re.findall(r'[0-9]+', open(r'TestData/regex_sum_1664978.txt').read())]))