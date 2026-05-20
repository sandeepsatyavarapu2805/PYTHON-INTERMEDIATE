import json, requests

'''
so you can use this but requests module is better

from urllib.request import Request, urlopen

req = Request("https://api.frankfurter.dev/v1/latest", headers={"User-Agent": "Mozilla/5.0"} )

with urlopen(req) as response:
    source = response.read()

since we are using urlopen the source we get is json which needs to be converted into python dict
    
data = json.loads(source)
print(data)

'''

response = requests.get('https://api.frankfurter.dev/v1/latest')

source_json = response.text
python_converted = response.json() # since we used response.json() without response.text we get the json converted into python

print(source_json)
print()
print(python_converted)
print()
print(json.dumps(python_converted, indent=1, sort_keys=True))