# coding=utf-8
import ssl
import requests
from bs4 import BeautifulSoup
import re

ssl._create_default_https_context = ssl._create_unverified_context
s = requests.session()

ean_gtin = "7891149200504"

html = s.get("https://cosmos.bluesoft.com.br/produtos/"+str(ean_gtin))
html = html.content
bsObj = BeautifulSoup(html, "html.parser")

# Buscar o link da imagem do produto
imagem_produto = bsObj.find("div", {"class": "product-thumbnail"}).findChild().attrs["src"] # localiza a <ul> que contém os links para as próximas páginas

print(imagem_produto)
'''
for pags in range(2):
    # for pags in range(int(paginas[len(paginas) - 2].text)):
    print(">>>>>>Página:" + str(pags) + "<<<<<<<")
    pagina_produtos = s.get("https://cosmos.bluesoft.com.br/ncms/" + num_NCM + "/products?page=" + str(pags))
    pag_content = pagina_produtos.content
    bsObj = BeautifulSoup(pag_content, "html.parser")

    produtos = bsObj.findAll("h5", {"class": "description"})

    for prod in produtos:
        print(prod.a.text + " - https://cosmos.bluesoft.com.br" + prod.a.attrs["href"])
    sleep(5)
'''

