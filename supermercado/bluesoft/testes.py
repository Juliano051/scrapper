# coding = utf-8
'''
Recebe como argumentos a url da imagem de um produto da internet e o codigo NCM no formato XXXX.XX.XX
Sera criada uma pasta com o NCM do produto e a imagem será salva em seu interior
'''
import ssl
import requests
import os

ssl._create_default_https_context = ssl._create_unverified_context
s = requests.session()


def salva_imagem(url, ncm):
    pasta = '.\\' + ncm + '\\'
    if not os.path.exists( pasta ):
        os.makedirs( pasta )
    else:
        print( "Pasta ja existe" )

    with open( pasta+url[-13:] + ".jpg", 'wb' ) as handle:

        response = s.get(url, stream=True)

        if not response.ok:
            print( response )

        for block in response.iter_content( 1024 ):
            if not block:
                break

            handle.write( block )


salva_imagem("https://cdn-cosmos.bluesoft.com.br/products/7891000101506", "ncm_ficticio")