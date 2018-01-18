import ssl
import requests
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context

s = requests.session()
html = s.get("https://cosmos.bluesoft.com.br/ncms/34022000/products?page=1")
html = html.content
bsObj = BeautifulSoup(html, "html.parser")

print(bsObj)

