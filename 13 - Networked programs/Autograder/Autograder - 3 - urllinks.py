# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def print_all(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        print(tag.get('href', None))

def enter_level(url, position):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    for index, tag in enumerate(tags):
        if index >= position:
            return tag.get('href', None)


#http://py4e-data.dr-chuck.net/known_by_Fikret.html
url = input('Enter URL: ')
AMOUNT_OF_TIMES = int(input("Enter count: "))
POSITION = int(input("Enter position: ")) -1
for _ in range(AMOUNT_OF_TIMES):
    url = enter_level(url, POSITION)
    print(f"Your URL at Position {POSITION} is: {url}")
    #print_all(url)
