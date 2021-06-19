# from modules.carrinho import listarCesta, addItem, checkout
import modules.carrinho as cr


def mainMenu():
    while True:
        print('Quitanda:')
        print('1 - ver cesta')
        print('2 - Adicionar fruta')
        print('3 - checkout')
        print('4 - Sair')
        opcao = int(input('Digite a Opção: '))
        if opcao == 1:
             cr.listarCesta()
        elif opcao == 2:
            cr.addItem()
        elif opcao == 3:
            cr.checkout()
        else:
            break

if __name__ == "__main__":
    mainMenu()