import re
regex_pattern = input("Enter a regular expression: ")
with open(r"RawTextFiles/mbox.txt") as f:
    matches = re.findall(regex_pattern, f.read())
print(len(matches))

    