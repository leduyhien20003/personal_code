import requests
import pprint


res = requests.get('http://google.com') # gui GET request den trang
print(res)
pprint.pprint(dict(res.request.headers)) # request header
print("-------------")
pprint.pprint(dict(res.headers)) # response header


