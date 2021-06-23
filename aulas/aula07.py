# Orientação ao Objeto
#importação arqivo csv
import csv 

# with open('texto.csv', 'r') as arquivo:
#     conteudo = csv.reader(arquivo, delimiter=',')
#     cabecalho = next (conteudo)
#     informacao01 = next(conteudo)
#     restante_info = []
#     for linha in conteudo:
#         restante_info.append(linha)

# print(cabecalho)
# print(informacao01)

# print(restante_info)

# import json
# import requests 

# cep=input('Informe um CEP: ')
# viacep = f'https://viacep.com.br/ws{cep}/json'
# conteudo = requests.get(viacep)
# with open('arquivo.json', 'w') as jsonfile:
#     jsonfile.write(conteudo)

#arquivoJson=json.load
    
# from defusedxml import ElementTree as ET 

# #carregando o arquivo
# arquivo_xml = ET.parse('arquivo.xml') 

# #acessando a tag root
# root = arquivo_xml.getroot()

# #iterando por todas as tgs da tag root 
# for elemento in root:
#     print(elemento.tag, elemento.text) 

# print ('===========')

# for time in root.find('times'):
#     print(time.tag, time.attrib) 

# print ('===========')

# for time in root.find('times'):
#    print(time.tag, time.attrib)
#    for jogador in time:
#        print (f'jogador: {jogador.text}\nQuantidade de gols: 1')

from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree

#estrutura raiz do xml

raiz = Element('cadastro')

#add comentarios ao xml
raiz.append(Comment('Cadastro de usuario da locadora xpto'))

#aad elementos da àrvore:

#Subelement nome
nome = SubElement(raiz, 'nome')
nome.text = 'Carlos Silva'

#Subelement CPF

cpf=SubElement(raiz, 'cpf')
cpf.text = '089.125.111-95'

#Subelement Endereço

endereco=SubElement(raiz,'endereço')
endereco.text = 'Rua Maria da Graca, 156 - Jd. Peri - SP'

#Subelement contato

contato = SubElement(raiz, 'contato')

#elemento com subelementos
telefone = SubElement(contato, 'telefone')
telefone.text = '(11) 953582497'

email = SubElement(contato, 'email')
email.text = 'carlos.silva@email.com'

#gerar arquivo xml
ElementTree(raiz).write('cadastro.xml')
