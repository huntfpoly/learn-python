import requests
import json
import sys

# if len(sys.argv) != 2:
#     sys.exit('Usage: itunes.py <search term>')

response = requests.get('https://itunes.apple.com/search?search=?entity=song&limit=10&term=freezer')
o = response.json()
for result in o['results']:
    print(result['trackName'])
# print(json.dumps(response.json(), indent=2))
