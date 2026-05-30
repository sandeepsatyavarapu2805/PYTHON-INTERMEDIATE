# https://httpbin.org/ link for httpbin
import requests

# ------------------------ GET ------------------------
payload_get = {'page' : 2, 'count' : 25}
response_get = requests.get('https://httpbin.org/get', params= payload_get)
print(response_get.text) # httpbin returns everything in json format

# ------------------------ POST ------------------------
payload_post = {'username' : 'Sandeep', 'password' : 'testing'}
response_post = requests.post('https://httpbin.org/post', data= payload_post)
print(response_post.text)

r_json = response_post.json() 
print(r_json['form'])
print()

# ------------------------ AUTH ------------------------
response_auth = requests.get('https://httpbin.org/basic-auth/Sandeep/testing', auth=('Sandeep', 'testing'))
print(response_auth.text)

response_unauth = requests.get('https://httpbin.org/basic-auth/Sandeep/testing', auth=('sandeep', 'testing'))
print(response_unauth) # <Response [401]> which means unauthorized response

# ------------------------ DELAY-TIMEOUT ------------------------
response_delay = requests.get('https://httpbin.org/delay/1', timeout= 4) # if delay => timeout errors
print(response_delay)