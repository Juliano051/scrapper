# coding=utf-8
# scrap_produto("https://cosmos.bluesoft.com.br/produtos/7891000101506-leite-em-po-desnatado-molico-nestle-280g")
import ssl
import requests
import re
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context
s = requests.session()

def scrap_produto(link):
    html = s.get(link)
    html = html.content
    bsObj = BeautifulSoup(html, "html.parser")

    # Buscar o link da imagem do produto

    info_produto = bsObj.find("dl", {"class": "dl-horizontal"})
    # for k in range(0, len(info_produto)-1, 2):
    #    pass
        # print( k, info_produto[k].text[1:-1], info_produto[k+1].text[1:-1] )
    # print(info_produto.findAll("dt"))
    info_produto = info_produto.findAll( "dt" )
    for t in info_produto:
        texto = (t.findNextSibling().text).re.sub('[!ale]', '', t.findNextSibling().text)
        print(t.text[1:-1], texto)

scrap_produto("https://cosmos.bluesoft.com.br/products/7891025610113")
