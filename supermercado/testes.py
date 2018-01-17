'''
Link obtido do site do supermercado Extra: O site www.deliveryextra.com.br possui um infinite scroll que é atualizado
através de queries feitas ao endereço:
https://api.gpa.digital/ex/products/list/secoes/C2475/?storeId=241&qt=34&s=&ftr=&p=2&rm=&gt=list-mobile
O link acima retorna um Json contendo Nome, Descrição, Classificação, e uma url relativa contendo imagens dos produtos
em tamanho P M e G. Essa url é relativa ao domínio deliveryextra.com.br e não ao gpa.digital
'''
import ssl
import requests
import json
from time import sleep

ssl._create_default_https_context = ssl._create_unverified_context

s = requests.session()
print("Iniciado...")
for count in range(99999):
    if count % 1000 == 0:
        print(count)
    sleep(0.2)
    html = s.get("https://api.gpa.digital/pa/products/list/secoes/"+str(count)+"/?storeId=501&qt=40&s=&ftr=&p=2&rm=&gt=list-mobile")
    if html.status_code == 200:
        print("https://api.gpa.digital/pa/products/list/secoes/" + str(count) + "/?storeId=501&qt=40&s=&ftr=&p=2&rm=&gt=list-mobile")
        js = json.loads(html.text)
        print(html)
        loop_categoria = len(js['content']['categories'])
        print("__" * 20)
        print(loop_categoria)
        for loop in range(loop_categoria):

            print("Categoria: " + js['content']['categories'][loop_categoria-1]['name'])

