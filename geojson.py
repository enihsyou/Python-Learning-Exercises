import urllib.request as ur
import urllib.parse as ul
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'
# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1 : address = 'Hebrew University'
    # if len(address) < 1 : break

    url = serviceurl + ul.urlencode({'sensor':'false', 'address': address})
    print('Retrieving', url)
    uh = ur.urlopen(url)
    data = uh.read().decode('utf-8')
    print('Retrieved',len(data),'characters')

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    print(js['results'][0]['place_id'])
    
