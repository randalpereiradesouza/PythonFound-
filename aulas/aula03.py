# Regras da linguagem

# Palavras reservadas não podem ser utilizadas para nomear outras coisas.
# Estrutuas de Condiçoes,repeticoes, funcoes, classes e contextos sempre terminam com :
# comandos que estão dentro de estruturas são identadas com 4 espaços
# # Objetos criados não podem começar com numeros, vigula, ponto...


# # Estrutura de Repetição

# ## While
# contador = 0

# while contador < 100:
#     print(contador)
#     contador += 1


# while True:
#     print("Sistema integrado de escolha")
#     print('Digite:')
#     print('1 - Para Escolher primeira opção')
#     print('2 - Para Escolher segunda opção')
#     print('0 - Para Sair')
#     opcao = int(input('>>> '))
#     if opcao == 1:
#         print('opçãos:')
#         print('1 - chocolate')
#         print('2 - dinheiro')
#         print('0 - voltar ao menu principal')
#         opcao2 = int(input('>>> '))
#         if opcao2 == 1:
#             print('O Tim estava certo')
#             break
#         elif opcao2 == 2:
#             print('O Tim estava errado')
#             break

#         else:
#             continue
#     elif opcao == 2:
#         print('Você escolheu a segunda opção')
#     elif opcao == 0:
#         break
#     else:
#         print('Opção Inválida')

## For

# texto = 'Olá eu sou um texto'

# for caracter in texto:
    # print(f'agora a variavel caracter é {caracter}')


# produtos = ['Camiseta A', 'Camiseta B', 'Camiseta C', 'Calca 1']


# for prod in produtos:
#     print(prod)


# Conjuntos - Coleções


# # Listas - Conjunto de objetos

# lista = ["String 1", "String 2", 2, 5, 1.6, True]

# # Métodos de lista
# lista.append('Arquivo 1')
# lista.insert(2, 'Dado')
# lista.remove('Dado')
# lista.pop(1)
# lista.sort('Dado')
# lista.clear()

# # Indexação de listas
# lista[0]
# lista[1][2][2][2]

# # Tuplas - Lista não alteravel

# # cadastro = ('Joao', 'Nascimento', 26)
# # cadastro.count()
# # cadastro.index()

# # Dicionarios

# nome = input("Digite seu nome: ")
# idade= input("Digite sua idade: ")
# email= input("Digite seu email: ")
# telefone= input("Digite seu telefone: ")

# dados_pessoais = {"nome": nome,
#                   "idade":  idade,
#                   "Telefone": telefone,
#                   "Email": email}

# dados_estaduais = {
#     "SP": {
#         "Nome": "Sao Paulo",
#         "Populacao": 150000,
#         "IDH": 15,
#         "Times": ['sao paulo', 'corinthians', 'palmeiras', 'santos']
#     },
#     "BH": {
#         "Nome": "Belo horizonte",
#         "Populacao": 10000,
#         "IDH": 12
#     },
#     "RJ": {
#         "Nome": "Rio de Janeiro",
#         "Populacao": 130000,
#         "IDH": 9
#     }
# }

# # Métodos de dict

# dados_pessoais.keys()
# dados_pessoais.values()
# dados_pessoais.get()
# dados_pessoais.clear()

# # Fatiamento de dicionario

# dados_pessoais["idade"]

# # Sets - Conjuntos de valores únicos

# conjunto = {1,2,4,5,6,7,8,9}















