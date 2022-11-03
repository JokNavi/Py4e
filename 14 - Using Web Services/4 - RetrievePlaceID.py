import urllib.request, urllib.parse, urllib.error
import json
import ssl



# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#South Federal University
#The University of Manchester
address = input('Enter location: ')
if len(address) < 1: exit()

parms = dict()
parms['address'] = address
if api_key is not False: parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)
    exit()

file_contents = json.dumps(js, indent=4)
print(file_contents)
with open(r"TestData/RetrievePlaceID.json", "w") as f:
    f.write(file_contents)



place_id = js['results'][0]['place_id']
print(place_id)