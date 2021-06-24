# Orientação a objetos

# Paradigma de programação - serve para resolver um tipo de problema

## Escrevemos codigos até agora usando paradigma procedural(reutiliza o código) e funcional 

#Problemas que o paradigma orientado a objetos resolve:
# - Reutilização do código (casses) 
# - Centralização dos dados
# - Aumento do tamanho do código

# Através do paradigma POO, temos:
# - Maior capacidade de manipular os dados de forma a respeitar as regras do negócio
# - Restringir o acesso aos dados

#Conceitos de POO:
#Abstração - Isolar a nossa lógica, mantendo o usuario sem a necessidade de compreender o todo.
#Encapsulamento -isolar seus atributos do cliente (ex. __atributo)
#Herança - Herdar atributos e metodos de outro objeto.
#Polimorfismo - Mesmo herdando caracteristicas, posso alterar essas caracteristicas na classe que herdou sem afetar a classe inicial

# class Casa01():
#     def__init__(self):
#     self.quartos = 2
#     self.sala = 1
#     self.banheiro = 2
#     self.garagem = 2
#     self.cozinha = 'americana'

#     def informacoes(self):
#         print(f'{self.quartos}')
#         print(f'{self.sala}')
#         print(f'{self.banheiro}')
#         print(f'{self.garagem}')
#         print(f'{self.cozinha}')

# #self - parametro de referencia - informa que o metodo esta associado 
#     def construirCasa(self):

# #a partir daqui tem-se um objeto - casa Pedro - Após instanciar 
# casaPedro = Casa01()

# class automovel():
#     #metodo construtor
#     nome ='automovel'
#     def__init__(self):
#        self.motor = True
#        self.rodas = 4
#        self.portas = 2
        
#     def ligar(self):
#         pass

#     def desligar(self):
#         pass

#     def acelerar(self):
#         pass
#     def frear(self):
#         pass

# hb20 = automovel()
# motor = True




# class contaCorrente():
    
#     def __init__(self):
#         self.__nomeCliente = input('Nome do cliente: ')
#         self.__idBanco = 777
#         self.__idAgencia =  int(input)('Digite o numero da agencia: ')
#         self.__saldo = 0 
    
#     def extrato(self):
#         print('----Extrato----')
#         print(f'Nome do cliente{self.__nomeCliente}')
#         print(f'Saldo{self.__saldo}')
    
#     def sacar(self, valor):
#         if self.__saldo>=valor:
#             print(f'Saldo anterior: {self.__saldo}')
#             self.__saldo -= valor
#             print(f'Novo saldo: {self.__saldo}')
#         else:
#             print('Saldo Insuficiente')

#     def depositar(self, valor): 
#         print(f'Saldo anterior: {self.__saldo}')
#         self.__saldo+= valor
#         print (f'Novo saldo:{self.__saldo}')


#herança

class Pai():
    def __init__(self):
        self.nome = 'João'
        self.sobrenome = 'Pereira Pinto'
        self.profissao = 'Marceneiro'
    def trabalha(self):
        print(f'Trabalha como{self.profissao}')

class Filho(Pai):   
    def __init__(self):
        super(). __init__()
# polimorfismo
        self.nome = 'Carlos'
        self.profissao = 'Menino do TI'







# class Colaborador():

#     def __init__(self):
#         self.__nome = input('Nome: ')
#         self.__matricula =input('Matricula: ')
#         self.__endereco = input('Endereço: ')
#         self.__dataNascimento = input ('Data de Nascimento: ')
#         self.__salario = 2500
#         self.funcao = 'N1'

#     def funcao(self):
#         print(f'Trabalhando {self.__funcao}')

# class ColaboradorN2(Colaborador):

#     def __init__(self):
#         Colaborador().__init__() 
#         #ou super().__init__()


#Palavras chave:

##Objeto - Uma instancia de uma classe
#Classe (class) - Definição de como o objeto deve ser 
#método Construtor - metodo que inicializa atributos na criação do objeto
#Instancia - variavel que contem a classe
#Atributo - caracteristica
#Método - ações do objeto 
#self - Referencia ao proprio objeto 