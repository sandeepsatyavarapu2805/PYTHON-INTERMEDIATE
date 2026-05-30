import requests
from pathlib import Path

response = requests.get('https://xkcd.com/353/') # import antigravity for the url

print(response)
# for any object if you print(help(response)) it gives detailed info about the object
print(response.status_code, response.ok) # ok returns true if the status code is < 400
print(response.connection)
print(response.headers)

BASE_DIR = Path(__file__).resolve().parent
filepath = BASE_DIR / 'comics.png'

img_response = requests.get('https://xkcd.com/353/comics/python.png')

with open(filepath, 'wb') as img:
    img.write(img_response.content)