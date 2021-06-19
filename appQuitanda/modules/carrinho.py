from .frutas import frutaMenu

cesta = []

def addItem():
    banana = {'nome':'banana', 'valor': 1.50}
    caju = {'nome':'caju', 'valor': 4.50}
    manga = {'nome':'manga', 'valor': 2.50}
    abacaxi = {'nome':'abacaxi', 'valor': 5.00}
    frutaMenu()
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

def listarCesta():
    for item in cesta:
        print(f"Produto: {item['nome']}, Valor: {item['valor']}")

def checkout():
    print('Checkout')
    total = 0
    for item in cesta:
        total += item['valor']
    print(f'Total da Compra: {total}')


# if __name__ == "__main__":

checkout()