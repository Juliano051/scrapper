# coding=utf-8
import ssl
import requests
from bs4 import BeautifulSoup


ssl._create_default_https_context = ssl._create_unverified_context
s = requests.session()


def scrap_produto(link):
    # html = s.get("https://cosmos.bluesoft.com.br/produtos/"+str(ean_gtin))
    html = s.get(link)
    html = html.content
    bsObj = BeautifulSoup(html, "html.parser")

    # Buscar o link da imagem do produto
    imagem_produto = bsObj.find("div", {"class": "product-thumbnail"}).findChild().attrs["src"]  # localiza o link da imagem do produto

    lista_ean_gtin = bsObj.find("table", {"class": "table-striped"}).find("tbody").findAll("tr")  # localiza o link da imagem do produto

    # ncm_produto = bsObj.find("h5", {"class": "description"}).find("p", {"class": "barcode"}).nextSibling

    info_produto = bsObj.find("dl", {"class": "dl-horizontal"}).findChildren()


    print(imagem_produto)

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
