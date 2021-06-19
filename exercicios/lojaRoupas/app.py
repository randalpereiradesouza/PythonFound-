# Criar um sistema de uma loja de roupas

# O sistema conterá as seguintes funções:

# verProdutos -> lista com dicionarios
    # {nome: Camiseta Hulk, tamanho: M, preco: 390}

# addProdutoCarrinho -> adiciona um produto ao seu carrinho

# addDesconto -> se utilizado no carrinho terá 20% de desconto

# removeProdutoCarrinho -> remove um produto do carrinho.

# checkout -> mostra total da compra

# mainMenu -> menu principal do sistema

from modules import produtos 

def mainMenu():
    while True:
        print('Menu principal')
        print('1 - Sistema de produtos')
        print('2 - Caixa Registradora')
        print('3 - Sair')
        opcao1 = int(input('Digite a opção: '))
       
        if opcao1 == 1:
            print('Menu de produtos')
            print('1 - Ver produtos')
            print('2 - Adicionar produto')
            print('3 - Remover Produtos')
            print('4 - voltar')
            opcao2 = int(input('>>>: '))
            produtos.produtos 
        elif opcao1 == 2:
            print('Caixa registradora')
            print('1 - Ver carrinho')
            print('2 - Adicionar Produto ao carrinho')
            print('3 - Remover Produtos do carrinho ')
            print('4 - Finalizar compra')
            print('5 - Sair')
            opcao3 = int(input('>>>>: '))
            pass
                   
        elif opcao3 ==3:
            break
