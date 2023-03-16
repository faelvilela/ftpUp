from ftplib import FTP
import os, sys
from datetime import datetime
import os.path, time
from backup import gerar_backup

today = datetime.now().strftime("%d-%m-%Y")
ftp = FTP('ftp.adress.com.br')  
ftp.login(user='user', passwd='password') 
print('CONECTADO')

def main():
    
    def up_Arquivo1():
        local = 'C:/Users/administrator/Desktop/Arquivo1'
        ftp.cwd('/Arquivo1/Inbound')  
        up(local, 'chamadas Arquivo1.csv')
        up(local, 'Endereços Arquivo1.csv')
        up(local, 'Pagamentos Arquivo1.csv')
        up(local, 'Telefones Arquivo1.csv')
        up(local, 'Email Arquivo1.csv')
        up(local, 'Pessoas Arquivo1.csv')
        up(local, 'Acionamentos Arquivo1.csv')
        print('Arquivo1 OK') 

    def up_Arquivo2():
        local = 'C:/Users/administrator/Desktop/Arquivo2'
        ftp.cwd('/Arquivo2/Inbound')  
        up(local, 'Chamadas Arquivo2.csv')
        up(local, 'Endereços Arquivo2.csv')
        up(local, 'Pagamento Arquivo2.csv')
        up(local, 'Telefones Arquivo2.csv')
        up(local, 'Email Arquivo2.csv')
        up(local, 'Pessoas Arquivo2.csv')
        up(local, 'Acionamentos Arquivo2.csv')
        print('Arquivo2 OK')
        
    def up_Arquivo3():
        local = 'C:/Users/administrator/Desktop/Arquivo3'
        ftp.cwd('/Arquivo3/Inbound')  
        up(local, 'Endereços Arquivo3.csv')
        up(local, 'Pagamentos Arquivo3.csv')
        up(local, 'Telefones Arquivo3.csv')
        up(local, 'Email Arquivo3.csv')
        up(local, 'Pessoas Arquivo3.csv')
        up(local, 'Acionamentos Arquivo3.csv') 
        print('Arquivo3 OK')

    #Checar presença de arquivos antes do envio
    check('C:/Users/administrator/Desktop/Arquivo1', 'Arquivo1')
    check('C:/Users/administrator/Desktop/Arquivo2', 'Arquivo2')
    check('C:/Users/administrator/Desktop/Arquivo3', 'Arquivo3')
    
    print('Continuar?(S/N)')
    x = input()
    if x == 's' or 'S':
        pass
    else:
        sys.exit()
    
    up_Arquivo1()
    up_Arquivo2()
    up_Arquivo3()
    
    ftp.quit()

    gerar_backup()
    
    print('FIM')

#Gerando um resumo dos arquivos dentro das subpastas com nome, data de modificação e tamanho
def check(path, nome):
    print('-----------------------------------------------------------------------------')
    print(nome+':')
    for directory, subdirectories, files in os.walk(path):
        for file in files:
            path2 = os.path.join(directory, file)
            modified = os.path.getmtime(path2)
            size = os.path.getsize(path2)
            name_arquivo = os.path.basename(path2).split('/')[-1]
            year,month,day,hour,minute,second=time.localtime(modified)[:-3]
            print("Data: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second),float(size*0.000001),'(', name_arquivo,')')

#Upload dos aquivos na ftp
def up(local, nome):
    with open(local+nome, 'rb') as file:
            ftp.storbinary('STOR '+nome, file)
    file.close()


if __name__ == '__main__':
    main()
