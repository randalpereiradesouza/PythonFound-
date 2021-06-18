#Escreva uma função que receba um numero e informe se é par ou impar

def par(n): 
    if n % 2 == 0:
        print ('Esse valor é par')
    else:
        print('Esse numero é impar')

num=int(input('Digite um numero: '))
par(num)


#

# Criar um sistema de uma loja de roupas

# O sistema conterá as seguintes funções:

# verProdutos -> lista com dicionarios
    # {nome: Camiseta Hulk, tamanho: M, preco: 390}

# addProdutoCarrinho -> adiciona um produto ao seu carrinho

# addDesconto -> se utilizado no carrinho terá 20% de desconto

# removeProdutoCarrinho -> remove um produto do carrinho.

# checkout -> mostra total da compra

# mainMenu -> menu principal do sistema