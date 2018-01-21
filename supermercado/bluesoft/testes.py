# coding = utf-8
import ssl
import requests
import os


ssl._create_default_https_context = ssl._create_unverified_context
s = requests.session()

foto = s.get("https://cdn-cosmos.bluesoft.com.br/products/7891000101506")

newpath = './temp/'
if not os.path.exists(newpath):
    os.makedirs(newpath)
else:
    print("Pasta ja existe")
foto.ret