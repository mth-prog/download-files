import os
import requests

dir = r'C:\Users\Usuario(a) Master\OneDrive\Área de Trabalho\GEMN'

os.makedirs(dir)

def download_file(url, endereço):
    respostaDOserver =  requests.get(url)

    with open(endereço, 'wb') as output:
        output.write(respostaDOserver.content)

if __name__ == "__main__":
    download_file("https://www.ime.usp.br/~slago/lp-13.pdf", 'teste.pdf')