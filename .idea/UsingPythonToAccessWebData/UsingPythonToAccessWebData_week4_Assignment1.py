from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# http://py4e-data.dr-chuck.net/comments_1688966.html
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

#Retreive all of the anchor tags
tags = soup('span')
sum = 0

for tag in tags:
    # print('Contents:', tag.contents[0])
    sum += int(tag.contents[0])
print(sum)
