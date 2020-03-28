import urllib.request, urllib.parse
import json
serverurl = 'http://py4e-data.dr-chuck.net/json?'

while True:
    address = input('Enter a location: ')
    if len(address) < 1:
        break
    url = serverurl + urllib.parse.urlencode({'address': address, 'key': 42})
    data = urllib.request.urlopen(url).read()
    try:
        js = json.loads(str(data))
    except:
        js = None

    if not js or "status" not in js or js['status'] != "OK":
        print("=== failure to retrieve ===")
        print(js)
        continue

    print(js)
