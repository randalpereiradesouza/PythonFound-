produtos = []

def addProduto(nome, tamanho, preco):
    produto = {
        'nome': nome,
        'tamanho': tamanho,
        'preço': preco
    }
    produtos.append(produto)

def verProdutos():
    for p in produtos:
        print('=========')
        print(f"Nome: {p['nome']}")
        print(f"tamanho: {p['tamanho']}")
        print(f"preco:{p['preco']}")

def removeProduto(produto):
    for p in produtos:
        if p['nome'] == produto:
            produto.remove(p)
            