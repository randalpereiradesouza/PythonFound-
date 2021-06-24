#crie uma classe colaborador que tenha atributos e métodos
#crie uma classe Gerente que herde do colaborador e altera a função e salario
#crie uma classe suporteN1 que herde do colaborador e altere função e salario

class colaborador():
    
    def __init__ (self, nome, idade, endereco):
        self.nome = nome
        self.nidade = idade
        self.endereco = endereco
        self.salario = 0
        self.funcao = None
        self.projeto = None

    def projetoAlocado(self):
        print(f'Colaborador{self.nome}\n função {self.funcao} \n projeto {self.projeto}')
    def alterarProjeto(self, projeto):
        self.projeto = projeto
        print(f'Projeto alocado: {self.projeto}')
    def demitir(self):
        print('Usuário demitido')

        # input('Digite o seu nome: ')
        # self.__matricula = input('Digite a matricula: ')
        # self.__salario = 0
        # self.__funcao = 'Trabalho Nivel1'

        # def trabalhar():
        #     print(f'O trabalhador{self.nome}, trabalha na funçõa {self.funcao} e salario{self.salario}')

class Gerente (colaborador):
    def __init__(self):    
        nome = input(f'Nome: ')  
        idade = input(f'Idade: ')
        edereço = input(f'Endereço: ')
        super().__init__(nome, idade, endereco)
        self.__salario = 6500
        self.__funcao = 'Gerente'
        # self.__salario = input('Altere o salário: ')
        # self.__funcao = input('Altere a função: ')

class suporteN1(colaborador):
    def __init__(self):
        super().__init__()
        self.__salario = input('altere o sálario: ')
        self.__funcao = input('Altere a função: ')

Inicio = Gerente()


