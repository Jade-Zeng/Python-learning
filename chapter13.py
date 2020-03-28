import urllib.request
import xml.etree.ElementTree as ET
html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_388314.xml').read()
tree = ET.fromstring(html)
counts = tree.findall('.//count')
number = 0
for count in counts:
    number = number + int(count.text)
print(number)