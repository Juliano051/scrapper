import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

ssl._create_default_https_context = ssl._create_unverified_context
html = urlopen("https://www.xvideos.com/tags/alone")
# html = open("xvs.html", encoding="utf-8")
bsObj = BeautifulSoup(html, "html.parser")

links = bsObj.findAll("div", {"class": "thumb-block"})
# links = bsObj.findAll("a", {"href": re.compile("https://www.xs.com/video[0-9]")})


print(links[23].prettify())

for link in links:
    print(link.find("a", {"href": re.compile("/video[0-9]"), "title": re.compile("[A*-z*]")}).attrs["title"])
    print("www.xvs.com/"+link.find("a", {"href": re.compile("/video[0-9]"), "title": re.compile("[A*-z*]")}).attrs["href"])
    # print(link.find("span", {"class": "mobile-hide"}).get_text())
    print(link.find("span", string=re.compile("[A*-z*]")).get_text())
    print(link.find("img", {"data-src": re.compile("[A*-z*]")}).attrs["data-src"])
    print("-"*20)
    # print(link.find("a", {"title": re.compile("[A*-z*]")}).attrs["title"])



'''
#
# print(bsObj)

# print(links[0].find("a", {"href": re.compile("/video[0-9]")}))
print(links[0].descendants)

print(len(links))
for link in links:
   print(link)
'''
