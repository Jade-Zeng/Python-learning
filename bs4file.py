import urllib.request
from bs4 import BeautifulSoup
urlinp = input('Enter url')
count = int(input('Enter repeat'))
position = int(input("Enter position"))
for line in range(count):
    html = urllib.request.urlopen(urlinp).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    s = []
    t = []
    for tag in tags:
        x = tag.get('href', None)
        s.append(x)
        y = tag.text
        t.append(y)

    a = s[position - 1]
    b = t[position - 1]
    print(a)
    print(b)
    urlinp = s[position - 1]