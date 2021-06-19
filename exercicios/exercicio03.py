

# Faça um sistema que pedirá as seguintes informações:

# Nome
# Idade
# Email
# Telefone
# nome = input("Digite seu nome: ")
# idade= input("Digite sua idade: ")
# email= input("Digite seu email: ")
# telefone= input("Digite seu telefone: ")


# while True:
#     print(f'Bem vindo {nome}')
#     print('Digite')
#     print('1 - Mostrar todas suas informações')
#     print('2 - Mostrar apenas o seu nome e idade')
#     print('3 - Mostrar seu email e telefone')
#     print('0 - Sair')
#     opcao = int(input('>>>'))
#     if opcao == 1:
#         print(f'Nome: {nome}\nIdade: {idade}\nTelefone: {telefone}\nEmail: {email}')
#         input('Digite Enter para voltar ao menu')
#     elif opcao == 2:
#         print(f'Nome: {nome}\nIdade: {idade}')
#         input('Digite Enter para voltar ao menu')
#     elif opcao == 3:
#         print(f'Telefone: {telefone}\nEmail: {email}')
#         input('Digite Enter para voltar ao menu')
#     elif opcao == 0:
#         break
#     else:
#         print('Opção Invalida!!')



# apresentará o seguinte menu:



# Bem vindo(a)! <nome>

# Opções:

# 1 - Mostrar todas suas informações
# 2 - Mostrar apenas o seu nome e idade
# 3 - Mostrar seu email e telefone
# 0 - Sair

# Exercicios Apostila

# 1

# data = int(input('Digite o ano de nascimento: '))


# if data <= 1964:
#     print('Baby Boomer')
# elif data >= 1965 and data <= 1979:
#     print('Geração X')
# elif data >= 1980 and data <= 1994:
#     print('Geração Y')
# elif data >= 1995:
#     print('Geração Z')
# else:
#     print('Informe uma data valida')

# 2 - Quitanda
# cesta = []
# total = 0

# while True:
#     print('Quitanda:')
#     print('1 - ver cesta')
#     print('2 - Adicionar fruta')
#     print('3 - checkout')
#     print('4 - Sair')
#     opcao = int(input('Digite a Opção: '))
#     if opcao == 1:
#         for item in cesta:
#             print(f"Produto: {item['nome']}, Valor: {item['valor']}")
#     elif opcao == 2:
#         print('Menu de frutas:')
#         print('1 - Banana')
#         print('2 - Caju')
#         print('3 - Manga')
#         print('4 - Abacaxi')
#         banana = {'nome':'banana', 'valor': 1.50}
#         caju = {'nome':'caju', 'valor': 4.50}
#         manga = {'nome':'manga', 'valor': 2.50}
#         abacaxi = {'nome':'abacaxi', 'valor': 5.00}
#         fruta = int(input('Digite a Opção: '))
#         if fruta == 1:
#             cesta.append(banana)
#         elif fruta == 2:
#             cesta.append(caju)
#         elif fruta == 3:
#             cesta.append(manga)
#         elif fruta == 4:
#             cesta.append(abacaxi)
#         else:
#             print('Opção invalida')
#     elif opcao == 3:
#         print('Checkout')
#         for item in cesta:
#             total += item['valor']
#         print(f'Total da Compra: {total}')
#         break

#         # print(f'Valor total: {}')

#     elif opcao == 4:
#         break



# Escreva um função que receba um número e informe
# Se é par ou ìmpar


def calculaPar(num):
    if num % 2 == 0:
        print(f'O numero {num} é Par')
    else:
        print(f'O numero {num} é Ímpar')


num = int(input('Digite um número'))
calculaPar(num)


# Criar um sistema de uma loja de roupas

# O sistema conterá as seguintes funções:

# verProdutos -> lista com dicionarios
    # {nome: Camiseta Hulk, tamanho: M, preco: 390}

# addProdutoCarrinho -> adiciona um produto ao seu carrinho

# addDesconto -> se utilizado no carrinho terá 20% de desconto

# removeProdutoCarrinho -> remove um produto do carrinho.

# checkout -> mostra total da compra

# mainMenu -> menu principal do sistema