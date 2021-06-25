# #Tratamentos de Exceções 
from datetime import datetime

try:
    arquivo = open('arquivo02', 'r+')
    arquivo.read()
    arquivo.write('Arquivo existente')
except Exception as e:
    print (e)
    arquivo = open('arquivo02', 'x+')
    arquivo.wite(f'arquivo criado em {datetime.now()}')
else:
    arquivo.close()
finally:
    print('Tratamento concluido')

#test 

