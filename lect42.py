import urllib.request
import urllib.parse

values = {'q':'python programing tutorials'}

data = urllib.parse.urlencode(values)
url = 'https://www.google.com/search?'+data
#date = data.encode('utf-8')

print(data)

req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
resp_data = resp.read()

print(resp_data)
