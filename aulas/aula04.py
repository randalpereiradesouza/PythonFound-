# cesta = []


# def addItem():
#     banana = {'nome':'banana', 'valor': 1.50}
#     caju = {'nome':'caju', 'valor': 4.50}
#     manga = {'nome':'manga', 'valor': 2.50}
#     abacaxi = {'nome':'abacaxi', 'valor': 5.00}
#     frutaMenu()
#     fruta = int(input('Digite a Opção: '))
#     if fruta == 1:
#         cesta.append(banana)
#     elif fruta == 2:
#         cesta.append(caju)
#     elif fruta == 3:
#         cesta.append(manga)
#     elif fruta == 4:
#         cesta.append(abacaxi)
#     else:
#         print('Opção invalida')

# def listarCesta():
#     for item in cesta:
#         print(f"Produto: {item['nome']}, Valor: {item['valor']}")

# def frutaMenu():
#     print('Menu de frutas:')
#     print('1 - Banana')
#     print('2 - Caju')
#     print('3 - Manga')
#     print('4 - Abacaxi')

# def checkout():
#     print('Checkout')
#     total = 0
#     for item in cesta:
#         total += item['valor']
#     print(f'Total da Compra: {total}')


# def mainMenu():
#     while True:
#         print('Quitanda:')
#         print('1 - ver cesta')
#         print('2 - Adicionar fruta')
#         print('3 - checkout')
#         print('4 - Sair')
#         opcao = int(input('Digite a Opção: '))
#         if opcao == 1:
#             listarCesta()
#         elif opcao == 2:
#             addItem()
#         elif opcao == 3:
#             checkout()
#         else:
#             break

# if __name__ == "__main__":
#     mainMenu()
import os

def ping(ip):
    os.system(f'ping {ip}')



ping('8.8.8.8')










