# coding=utf-8
import ssl
import requests
import re
from bs4 import BeautifulSoup
import bs_scrap_salva_imagem

ssl._create_default_https_context = ssl._create_unverified_context
s = requests.session()

def scrap_produto(link):
    # html = s.get("https://cosmos.bluesoft.com.br/produtos/"+str(ean_gtin))
    html = s.get(link)
    html = html.content
    bsObj = BeautifulSoup(html, "html.parser")

    # Buscar o link da imagem do produto
    nome_prduto = bsObj.find( "meta", {"property": "og:title"})
    cest_produto = bsObj.find("span", {"class": "description cest-name"})
    ncm_produto = bsObj.find("a", {"title": "Mais produtos da NCM"}).findChild()
    imagem_produto = bsObj.find("div", {"class": "product-thumbnail"}).findChild().attrs["src"]  # localiza o link da imagem do produto
    lista_ean_gtin = bsObj.find("table", {"class": "table-striped"}).find("tbody").findAll("tr")  # localiza o link da imagem do produto
    info_produto = bsObj.find("dl", {"class": "dl-horizontal"}).findChildren()

    print("Produto: "+nome_prduto.attrs["content"])
    print("CEST: "+cest_produto.text[1:9])
    print("NCM: "+str(ncm_produto.text[1:-1]))
    print(imagem_produto)
    bs_scrap_salva_imagem.salva_imagem(imagem_produto, str(ncm_produto.text[1:-1]))
    print(info_produto[0].text[1:-1], info_produto[1].text[1:-1])
    print(info_produto[2].text[1:-1], info_produto[3].text[1:-1])
    print(info_produto[4].text[1:-1], info_produto[5].text[1:-1])
    print(info_produto[6].text[1:-1], info_produto[8].text[1:-1])
    print(info_produto[10].text[1:-1], info_produto[12].text[1:-1])

    for i in range(len(lista_ean_gtin)):
        print("GTIN: "+lista_ean_gtin[i].findAll("td")[0].text[1:-1])
        print("Unidade: "+lista_ean_gtin[i].findAll("td")[1].text[1:-1])
        print("Qtde.: "+lista_ean_gtin[i].findAll("td")[2].text[1:-1])
        print("Bruto: "+lista_ean_gtin[i].findAll("td")[8].text[1:-1])
        print("Líquido: "+lista_ean_gtin[i].findAll("td")[9].text[1:-1])


scrap_produto("https://cosmos.bluesoft.com.br/produtos/7891000101506-leite-em-po-desnatado-molico-nestle-280g")
