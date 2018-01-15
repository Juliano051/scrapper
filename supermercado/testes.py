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
secao = "C2475"
storeId = "241"
s = requests.session()
# html = s.get("https://api.gpa.digital/ex/products/list/secoes/"+secao+"/?storeId="+storeId+"&qt=34&s=&ftr=&p=2&rm=&gt=list-mobile")
html = s.get("https://api.gpa.digital/ex/products/list/secoes/C2475/?storeId=241&qt=35&s=&ftr=&p=1&rm=&gt=list-mobile")
js = json.loads(html.text)
print("Total de itens: "+str(js['content']['totalElements']))
print("Núm. de páginas: "+str(js['content']['totalPages']))
print("Itens por pág: "+str(js['content']['size']))

loop_pags = js['content']['totalPages']
loop = js['content']['size']-1


html = s.get("https://api.gpa.digital/ex/products/list/secoes/C2475/?storeId=241&qt=35&s=&ftr=&p=14&rm=&gt=list-mobile")
js = json.loads(html.text)

for x in range(loop):
    print("__"*20)

    print("Item:"+str(x))
    if js['content']['products'][loop]['shelfList'][2]['name']:
        print("Cat. Principal: "+js['content']['products'][loop]['shelfList'][2]['name'])
    if js['content']['products'][loop]['shelfList'][1]['name']:
        print("Subcategoria: "+js['content']['products'][loop]['shelfList'][1]['name'])
    if js['content']['products'][loop]['shelfList'][0]['name']:
        print("Classificação: "+js['content']['products'][loop]['shelfList'][0]['name'])
    print("Produto: "+js['content']['products'][loop]['name'])
    if js['content']['products'][loop]['shortDescription']:
        print("Descrição: "+js['content']['products'][loop]['shortDescription'])
    print("Imagem grande: http://www.deliveryextra.com.br"+js['content']['products'][loop]['mapOfImages']['0']['BIG'])
    print("Imagem média: http://www.deliveryextra.com.br"+js['content']['products'][loop]['mapOfImages']['0']['MEDIUM'])
    print("Thumbnail: http://www.deliveryextra.com.br"+js['content']['products'][loop]['mapOfImages']['0']['SMALL'])
    print("__" * 20)

