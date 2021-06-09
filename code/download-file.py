import shutil
import requests
import os
from pynput.keyboard import Key, Controller

dir = r'C:\Users\Usuario(a) Master\OneDrive\Área de Trabalho\Teste'

os.makedirs(dir)

def download_file(url, endereço, pasta):
    respostaDOserver =  requests.get(url)

    with open(endereço, 'wb') as output:
        output.write(respostaDOserver.content)
    shutil.move(endereço , pasta) #mover o arquivo para a pasta desejada
    #os.startfile(dir + "/" + endereço) #abre o arquivo 
  
download_file("https://drive.google.com/u/0/uc?id=1QEvcAhZaVqgovN6PqltFqOnHq9IepXdz&export=download", "teste.accdb", dir)

'''keyb = Controller()

keyb.press('l')'''