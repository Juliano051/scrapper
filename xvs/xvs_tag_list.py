import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re  # pacote de expressoes regulares

ssl._create_default_https_context = ssl._create_unverified_context  # Suprime os alertas de erro de SSL
# html = urlopen("https://www.xvideos.com/tags/") # abre a url
html = open("xvs_tags.html", encoding="utf-8")
bsObj = BeautifulSoup(html, "html.parser")

# links = bsObj.findAll("a", {"href": re.compile("https://www.xs.com/video[0-9]")})
# links = bsObj.findAll('a', {"href": re.compile("/tags/")})

# O processo consiste em listar as tags herdeiras das classes "navbadge default"
# que normalmente sao encontradas nas tags <a> que contém links para as categorias de páginas
# em seguida listar suas parents que contém a expressão "/tags/" em seus atributos href, ou seja,
# os próprios links das categorias

links = bsObj.findAll('span', {"class": "navbadge default"})  # classe child do link que contém a tag

print(len(links))
for link in links:
    link = link.find_parent('a', {"href": re.compile("/tags/")})
    if link is None:
        pass
    else:
        print(link.contents[0].get_text()+" - "+link.attrs["href"])
