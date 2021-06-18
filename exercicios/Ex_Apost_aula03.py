# #Exercico apostila

#ex 01

# data = int(input('Digite o ano de nascmento: '))

# if data <= 1964:
#     print('Baby Boomer')
# elif data <= 1965 and data <= 1979:
#     print('Geração X')
# elif data <= 1980 and data <= 1994:
#     print('Geração Y')   
# elif data <= 1995:
#     print('Geração z')  
# else:
#     ('Informe uma data válida')

# Ex 02

# cesta = []


# while True:
#     print('Quitanda: ')
#     print('1- Ver cesta')
#     print('2- Adicionar fruta')
#     print('3- Sair')
#     # cesta = [] a cesta não pode ficar aqui pq toda vez que rodar o codigo a cesta vai esvaziar

#     opcao = int (input('Digite a opção: '))
#     if opcao == 1:
#         print(cesta)
#     elif opcao == 2 :
#         print('Menu de Frutas:')
#         print(' 1 - banana')
#         print(' 2 - caju')
#         print(' 3 - Manga')
#         print(' 4 - abacaxi')
#         fruta = int(input('Digite a opção: '))
#         if fruta ==1:
#             cesta.append('Banana')
#         elif fruta ==2:
#             cesta.append('Caju')
#         elif fruta ==3:
#             cesta.append('Manga')
#         elif fruta ==4:
#             cesta.append('Abacaxi')
#         if fruta ==1:
#             cesta.append('Banana')
#         else:
#             print('Opção inválida')
#     elif opcao == 3:
#         break


#  exercicio 3 (inicio)

# cesta = []

# while True:
#     print('Quitanda: ')
#     print('1- Ver cesta')
#     print('2- Adicionar fruta')
#     print('3- Checkout')
#     print('4- Sair')
#     # cesta = [] a cesta não pode ficar aqui pq toda vez que rodar o codigo a cesta vai esvaziar

#     opcao = int (input('Digite a opção: '))
#     if opcao == 1:
#         print(cesta)
#     elif opcao == 2 :
#         print('Menu de Frutas:')
#         print(' 1 - banana')
#         print(' 2 - caju')
#         print(' 3 - Manga')
#         print(' 4 - abacaxi')
#         banana = {'nome': 'Banana', 'valor' : 1.50 } 
#         fruta = int(input('Digite a opção: '))
#         if fruta ==1:
#             cesta.append('Banana')
#         elif fruta ==2:
#             cesta.append('Caju')
#         elif fruta ==3:
#             cesta.append('Manga')
#         elif fruta ==4:
#             cesta.append('Abacaxi')
#         if fruta ==1:
#             cesta.append('Banana')
#         else:
#             print('Opção inválida')
#     elif opcao == 3:
#         break

    # 2 - Quitanda
cesta = []
total = 0

while True:
    print('Quitanda:')
    print('1 - ver cesta')
    print('2 - Adicionar fruta')
    print('3 - checkout')
    print('4 - Sair')
    opcao = int(input('Digite a Opção: '))
    if opcao == 1:
        for item in cesta:
            print(f"Produto: {item['nome']}, Valor: {item['valor']}")
    elif opcao == 2:
        print('Menu de frutas:')
        print('1 - Banana')
        print('2 - Caju')
        print('3 - Manga')
        print('4 - Abacaxi')
        banana = {'nome':'banana', 'valor': 1.50}
        caju = {'nome':'caju', 'valor': 4.50}
        manga = {'nome':'manga', 'valor': 2.50}
        abacaxi = {'nome':'abacaxi', 'valor': 5.00}
        fruta = int(input('Digite a Opção: '))
        if fruta == 1:
            cesta.append(banana)
        elif fruta == 2:
            cesta.append(caju)
        elif fruta == 3:
            cesta.append(manga)
        elif fruta == 4:
            cesta.append(abacaxi)
        else:
            print('Opção invalida')
    elif opcao == 3:
        print('Checkout')
        for item in cesta:
            total += item['valor']
        print(f'Total da Compra: {total}')
        break

        # print(f'Valor total: {}')

    elif opcao == 4:
        break

