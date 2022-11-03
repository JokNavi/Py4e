
import urllib.request, urllib.parse, urllib.error
import json

#http://py4e-data.dr-chuck.net/comments_42.json
url = input('Enter location: ')
print(f"Retrieving {url}")
response = urllib.request.urlopen(url)
info = json.loads(response.read())

print(f"Retrieved {len(info)} characters")

#file_contents = json.dumps(info, indent=4)
#with open(r"TestData/AddNumberJSON.json", "w") as f:
#    f.write(file_contents)


count = int()
number_list = list()
for item in info['comments']:
    count += 1
    number_list.append(item['count'])

print(f"Count: {count}")
print(f"Sum: {sum(number_list)}")
