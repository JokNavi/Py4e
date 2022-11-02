import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen(r'http://data.pr4e.org/romeo.txt')
fhand = open(r'TestData/romeo.txt', 'wb')
content = bytes()
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    content = content + info

fhand.write(content[:3000])
print(size, 'characters copied.')
fhand.close()