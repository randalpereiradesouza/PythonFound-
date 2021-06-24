#criar uma aplicação que consuma a api do viacep

#Funções
        # InformaRua - recebe um cep e infrorma a rua
        # informaBairro - recebe um cep e informa o bairro

        #consulta CEP full - recebe o cep e informa o endereço completo

       
import json
import requests

def main():
    while True:
        CEP = input('Informe um CEP: ')
        x = consultaCEP(CEP)
        print('Menu de consulta CEP')
        print('1 - consultar endereço completo')
        print('2 - Consultar nome da rua')
        print('3 - Consultar nome do Bairro')
        print('4 - Sair')
        opcao = input('>>>')
        if opcao == '1':
            print(x)
        elif opcao =='2':
            print(x['logradouro'])
        elif opcao == '3':
            print(x['bairro'])
        elif opcao == '4':
            break
        else: 
            print('opcao invalida')


def consultaCEP(cep):
    viacep = f'https://viacep.com.br/ws/{cep}/json'
    req = requests.get(viacep).text
    #conteudo = json.loads(req.content)
    reqjson = json.loads(req)
    return reqjson

main()

