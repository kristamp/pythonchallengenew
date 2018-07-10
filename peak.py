import pickle
import urllib.request

req = urllib.request.Request('http://www.pythonchallenge.com/pc/def/peak.html')
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))
req = urllib.request.Request('http://www.pythonchallenge.com/pc/def/banner.p')
response=urllib.request.urlopen(req)
banner=pickle.loads(response.read())

for line in banner:
    for pattern in line:
        (c,n)=pattern
        for i in range (n):
            print (c,end="")
    print ()