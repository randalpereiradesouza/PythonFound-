class Item():
    
    #método construtor
    def __init__(self, nome, descricao ='', preco = 0):
        self.__item
        self.__nome = nome,
        self.__descricao = descricao,
        self.__preco = preco
        
    def make_item(sef):
        self.item = {
            'nome': self.__nome,
            'preco': self.__preco
        }
        return self.item
        
    #métodos de acesso

    def get_item(self):
        return self.__item 

    def get_nome(self):
        return self.__item['nome']

    def get_desc(self):
        return self.__item['descricao']
    
    def get_preco(self):
        return self.__item['preco']
    
    #métodos de definição
    def set_nome(self, nome):
        self.__nome = nome
    
    def set_preco(self, preco):
        self.__preco = preco

    def set_desc(self, descricao):
        self.__descrição = descricao


