import urllib.request

response: object=urllib.request.urlopen('http://ww.baidu.com')
print(response.status)
print(response.read())
print(response.headers())
