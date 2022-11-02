import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import socket
import time
import ssl
import re

def HTTP_request_text():
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()
    # Code: http://www.py4e.com/code3/socket1.py

def HTTP_request_image():
    HOST = 'data.pr4e.org'
    PORT = 80
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((HOST, PORT))
    mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
    count = 0
    picture = b""

    while True:
        data = mysock.recv(5120)
        if len(data) < 1: break
        time.sleep(0.25)
        count = count + len(data)
        print(len(data), count)
        picture = picture + data

    mysock.close()

    # Look for the end of the header (2 CRLF)
    pos = picture.find(b"\r\n\r\n")
    print('Header length', pos)
    print(picture[:pos].decode())

    # Skip past the header and save the picture data
    picture = picture[pos+4:]
    fhand = open(r"TestData/stuff.jpg", "wb")
    fhand.write(picture)
    fhand.close()
    # Code: http://www.py4e.com/code3/urljpeg.py

def urllib_request_text():
    fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
    for line in fhand:
        print(line.decode().strip())

def urllib_request_binary():
    img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
    fhand = open(r'TestData/cover3.jpg', 'wb')
    fhand.write(img)
    fhand.close()

def urllib_request_binary_better():
    img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
    fhand = open('cover3.jpg', 'wb')
    size = 0
    while True:
        info = img.read(100000)
        if len(info) < 1: break
        size = size + len(info)
        fhand.write(info)

    print(size, 'characters copied.')
    fhand.close()
    
def urllib_find_URLs():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter - ')
    html = urllib.request.urlopen(url, context=ctx).read()
    links = re.findall(b'href="(http[s]?://.*?)"', html)
    for link in links:
        print(link.decode())

def urllib_find_flawed_URLs():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter - ')
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        print(tag.get('href', None))

urllib_find_flawed_URLs()

def urllib_find_flawed_URL_info():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter - ')
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        # Look at the parts of a tag
        print('TAG:', tag)
        print('URL:', tag.get('href', None))
        print('Contents:', tag.contents[0])
        print('Attrs:', tag.attrs)

urllib_find_flawed_URL_info()
