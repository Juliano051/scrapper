# coding=utf-8
import ssl
import requests
from bs4 import BeautifulSoup
from time import sleep

ssl._create_default_https_context = ssl._create_unverified_context
s = requests.session()

# num_NCM = "34022000"

def scrap_produtos_por_ncm(num_NCM):
    html = s.get("https://cosmos.bluesoft.com.br/ncms/" + num_NCM + "/products")
    html = html.content
    bsObj = BeautifulSoup(html, "html.parser")

    # Listar a quantidade de paginas que compoem a paginacao
    paginacao = bsObj.find("ul", {"class": "pagination"})  # localiza a <ul> que contém os links para as próximas páginas
    paginas = paginacao.findAll("li", recursive=False)  # Lista apenas os <li> que contém os links
    print(paginas[len(paginas) - 2].text)  # Busca o número da última página contido no último botão
    nome_ncm = bsObj.find("title")  # Busca o nome do NCM
    print(nome_ncm.text[:-20] + "\n")

    for pags in range(2):
    # for pags in range(int(paginas[len(paginas) - 2].text)):
        print(">>>>>>Página:" + str(pags) + "<<<<<<<")
        pagina_produtos = s.get("https://cosmos.bluesoft.com.br/ncms/" + num_NCM + "/products?page=" + str(pags))
        pag_content = pagina_produtos.content
        bsObj = BeautifulSoup(pag_content, "html.parser")

        produtos = bsObj.findAll("h5", {"class": "description"})

        for prod in produtos:
            print(prod.a.text + " - https://cosmos.bluesoft.com.br" + prod.a.attrs["href"])
            sleep(0.1)


scrap_produtos_por_ncm("04011010")
