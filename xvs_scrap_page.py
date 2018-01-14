import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

ssl._create_default_https_context = ssl._create_unverified_context
html = urlopen("https://www.xvideos.com/tags/alone")
# html = open("xvs.html", encoding="utf-8")
bsObj = BeautifulSoup(html, "html.parser")

# links = bsObj.findAll("a", {"href": re.compile("https://www.xs.com/video[0-9]")})
links = bsObj.findAll('a')
#
print(len(links))
for link in links
   print(link)