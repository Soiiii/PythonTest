import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

lis = []
url = input('Enter - ')
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()

tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
count = 0
sum = 0
for item in lst:
    num = item.find('count').text
    lis.append(num)
    l = len(lis)
for count in range(l) :
    sum += int(lis[count])
print(sum)