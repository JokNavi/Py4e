import socket
import re
characters = list()
url = input("URL -")
try:
    url = re.search(r'(\w+\.\w+(\.\w+)?)', url)[0]
except:
    print("Wrong URL format.")
    exit()

# data.pr4e.org
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((url, 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    characters.extend([char for char in data.decode()])
mysock.close()
print(*characters[:3000], sep='', end='')
print(f'Amount of characters: {len(characters)}')

# Code: http://www.py4e.com/code3/socket1.py
