import json
import requests

r = requests.get('http://ip.jsontest.com/')

blah = r.json()
print(blah['ip'])

r2 = requests.get('http://headers.jsontest.com/')
blah2 = r2.json()
print(blah2['Host'])