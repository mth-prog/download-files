import shutil
import requests
import os
from zipfile import ZipFile


dir = r'C:\Users\Usuario(a) Master\OneDrive\Área de Trabalho\Teste'

os.makedirs(dir)

def download_file(url, nome, pasta):
    respostaDOserver =  requests.get(url)

    with open(nome, 'wb') as output:
        output.write(respostaDOserver.content)
    shutil.move(nome , pasta) #mover o arquivo para a pasta desejada
    # os.startfile(dir + "/" + endereço) #abre o arquivo 
    
download_file("https://drive.google.com/u/0/uc?id=1QEvcAhZaVqgovN6PqltFqOnHq9IepXdz&export=download", "teste.zip", dir)

