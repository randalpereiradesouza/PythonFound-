# As 4 maneiras de trabalhar com funções

# 1 - Utilizando as funções built-in

# print()
# input()

# 2 - Importando apartir de modulos

# import os

# os.system('ls -la')


# 3 - Criando suas proprias funçoes

# def soma(x,y):
#     return x + y

# 4 - Utilizando funçoes anonimas
  
# soma = lambda x, y: x + y


# Escopo

# var1 = 'Eu sou uma variavel ambulante'


# def soma(x,y):
#     xablau = x + y
#     return xablau

# x = soma(10, 10)
# print(x)


# Parametros não Obrigatorios


# def multiplica(x,y,desconto=1):
#     total = total * desconto

# def soma(y=1, x=1):
#     print 

# print(multiplica(10, 15))


# Parâmetros com palavra-chave

def calculoPosicao(*, latitude, longetude):
    posicao = latitude - longetude
    print(posicao)



# calculoPosicao(longetude=446466, latitude=144545)



# Multiplos argumentos

# Args
def soma(*num):
    total = 0
    for i in num:
        total += i
    print(total)

# soma(1,2,3,4,5,6,76,7,5,54,5,54,4,4,4)


# Multiplos argumentos com palavras-chaves

# kwargs


def checkout(**valores):
    print(valores)

checkout(produto='camiseta', preco=150)
