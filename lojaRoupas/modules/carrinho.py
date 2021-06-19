


def verCarrinho():
    for c in carrinho:
        print('=======')
        print(f"Nome: {c['nome']}")
        print(f"Tamanho: {c['tamanho']}")
        print(f"Preco: {c['preco']}")
        

def addProdutoCarrinho(produto):
    carrinho.append(produto)
    print(carrinho)
    

def removeProdutoCarrinho(produto):
    carrinho.remove(produto)
    print(carrinho)

def checkout():
    total = 0
    for c in carrinho:
        total += c['preco']
    print(f'total: {total}')