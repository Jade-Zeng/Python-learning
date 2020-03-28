import urllib.request
import json
url = 'http://py4e-data.dr-chuck.net/comments_388315.json'
data = urllib.request.urlopen(url).read()
js = json.loads(data)
counts = 0
comment = js['comments']
for line in comment:
    counts = counts + line['count']
print(counts)