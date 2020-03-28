import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
html = urllib.request.urlopen(' http://py4e-data.dr-chuck.net/comments_388312.html').read()
soup = BeautifulSoup(html,"html.parser")
tags = soup('span')
sum = 0
count = 0
for item in tags:
    x = int(item.text)
    sum = sum + x
    count = count + 1
print(count)
print(sum)
