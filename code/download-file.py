import shutil
import requests
import os
import zipfile
import struct
import win32com.client


def is_64bit_pe(filename):  #~ Ira retorna true pra 64 e false para 32
    import win32file
    return win32file.GetBinaryType(filename) == 6


VersionOS = (struct.calcsize("P")*8) #~ procura a versão do SO


xl = win32com.client.Dispatch("access.Application") #~ procura a versão do Office
access_version = xl.version


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
        #os.startfile(dir + "/" + "teste.accdb") #~caso queria abrir o programa


if VersionOS == 64:
    #arquivos 64
else:
    #arquivos 32 



# versão do office 

access_version

#is 32 or 64


is_64bit_pe(r'C:\Program Files\Microsoft Office\root\Office16\MSACCESS.EXE')


# inicio para rodar os cmd 