import urllib.request
import io
import zipfile
filename="90052.txt"
req = urllib.request.Request('http://www.pythonchallenge.com/pc/def/channel.html')
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))
message=[]
req = urllib.request.Request('http://www.pythonchallenge.com/pc/def/channel.zip')
response = urllib.request.urlopen(req)

with zipfile.ZipFile(io.BytesIO(response.read())) as thezip:

    for i in range (2000):
        try:
            with thezip.open(filename) as f:
                message.append(thezip.getinfo(filename).comment.decode('utf-8'))
                for line in f:
                    print (line)
                    words=line.decode('utf-8').split()
                    filename=words[-1]+".txt"
        except:
            print(''.join(message))

