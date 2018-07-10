import urllib.request

req = urllib.request.Request('http://www.pythonchallenge.com/pc/def/oxygen.html')
response = urllib.request.urlopen(req)
