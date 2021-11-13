import shutil
import requests
import os
import zipfile
import struct


dir = r'C:\Users\Usuario(a) Master\OneDrive\Área de Trabalho\Teste'

os.makedirs(dir)

def download_file(url, nome, pasta):
    respostaDOserver =  requests.get(url)

    with open(nome, 'wb') as output:
        output.write(respostaDOserver.content)
    shutil.move(nome , pasta) #mover o arquivo para a pasta desejada
    #os.startfile(dir + "/" + nome) #abre o arquivo 
    
download_file("https://drive.google.com/u/0/uc?id=1CDGAvfTmCLXfuRwXkWCwSgVBXW0_YD0D&export=download", "teste.zip", dir)


dir_name = dir
extension = ".zip"

os.chdir(dir_name) 

for item in os.listdir(dir_name):
    if item.endswith(extension):
        file_name = os.path.abspath(item) 
        zip_ref = zipfile.ZipFile(file_name)
        zip_ref.extractall(dir_name)
        zip_ref.close()
        os.remove('teste.zip')
        