produtos = []

def addProduto(nome, tamanho, preco):
    """ Função responsavel por adicionar produtos a minha lista de produtos
    Params: 
        nome - nome do produto
        tamanho - tamanho do produto
        preco - preco do produto
    Return:
        None
    """
    produto = {
        'nome': nome,
        'tamanho': tamanho,
        'preco': preco
    }
    produtos.append(produto)

def verProdutos():
    for p in produtos:
        print('=======')
        print(f"Nome: {p['nome']}")
        print(f"tamanho: {p['tamanho']}")
        print(f"preco:  {p['preco']}")
        
    

def removerProduto(produto):
    for p in produtos:
        if p['nome'] == produto:
            produtos.remove(p)
