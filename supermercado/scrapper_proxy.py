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
import re

ssl._create_default_https_context = ssl._create_unverified_context
secao = "C245"
s = requests.session()
html = s.get("https://api.gpa.digital/ex/products/list/secoes/C2475/?storeId=241&qt=34&s=&ftr=&p=2&rm=&gt=list-mobile")
js = json.loads(html.text)
print(js['content']['products'][0]['name'])
print(js['content']['products'][0]['shortDescription'])
print("http://www.deliveryextra.com.br"+js['content']['products'][0]['mapOfImages']['0']['BIG'])
print("http://www.deliveryextra.com.br"+js['content']['products'][0]['mapOfImages']['0']['MEDIUM'])
print("http://www.deliveryextra.com.br"+js['content']['products'][0]['mapOfImages']['0']['SMALL'])

