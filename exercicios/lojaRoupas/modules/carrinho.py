carrinho = []

def verCarrinho():
    for c in carrinho:
        print ('=====')
        print (f"Nome: {c['nome']}")
        print (f"Tamanha: {c['tamanho']}")
        print (f"Preço: {c['preco']}")

def addProdutoCarrinho(produto):
    carrinho.append(produto)
    print(carrinho)

def removeProduto(produto)
    carrinho.remove (produto)
    print(carrinho)



