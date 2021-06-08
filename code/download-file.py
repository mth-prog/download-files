import shutil
import requests
import os

dir = r'C:\Users\Usuario(a) Master\OneDrive\Área de Trabalho\Teste'

os.makedirs(dir)

def download_file(url, endereço, pasta):
    respostaDOserver =  requests.get(url)

    with open(endereço, 'wb') as output:
        output.write(respostaDOserver.content)
    shutil.move(endereço , pasta) #mover o arquivo para a pasta desejada

if __name__ == "__main__":
    
    download_file("https://www.ime.usp.br/~slago/lp-13.pdf", 'teste.pdf', dir)