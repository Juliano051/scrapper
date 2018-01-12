import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

ssl._create_default_https_context = ssl._create_unverified_context
# html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
html = open("xvs.html", encoding="utf-8")
bsObj = BeautifulSoup(html, "html.parser")

links = bsObj.findAll("a", {"href": re.compile("https://www.xvideos.com/video[0-9]")})
print(len(links))
for link in links:
    print(link)
#if 'href' in link.attrs:
#    print(link.attrs['href'])