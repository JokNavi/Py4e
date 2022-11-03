import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/comments_42.xml?'
#serviceurl = input("Enter location: ")
print(f"Retrieving http://{serviceurl}")

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)

    print(f"Retrieved {len(data)} characters")
    numbers = list()
    for count_tag in tree.findall('.//count'):
        print(count_tag.text)
        numbers.append(int(count_tag.text))
    print(f"Count: {len(numbers)}")
    print(f"Sum: {sum(numbers)}")
    break