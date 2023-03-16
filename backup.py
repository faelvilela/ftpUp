import os, shutil
from datetime import datetime


def gerar_backup():
    today = datetime.now().strftime("%d-%m-%Y")

    child = 'X:/'
    path = os.path.join(child, today)
    os.mkdir(path) #criando pasta em X:/ com a data de hoje como nome

    arquivo1 = os.path.join(path, 'Arquivo1')
    os.mkdir(arquivo1)
    arquivo2 = os.path.join(path, 'Arquivo2')
    os.mkdir(arquivo2)
    arquivo3 = os.path.join(path, 'Arquivo3')
    os.mkdir(arquivo3) #criando subpastas para cada arquivo

    print('Comecando a copiar')
    copia('C:/Users/administrator/Desktop/Arquivo1', arquivo1)
    copia('C:/Users/administrator/Desktop/Arquivo2', arquivo2)
    copia('C:/Users/administrator/Desktop/Arquivo3', arquivo3)
    print('Arquivos Copiados')

def copia(source_folder, destination_folder):

    for file_name in os.listdir(source_folder):
        # construindo caminho dos arquivos
        source = os.path.join(source_folder, file_name)
        destination = os.path.join(destination_folder, file_name)
        # copiando arquivos  
        shutil.copy(source, destination)