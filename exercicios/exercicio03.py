# Faça um sistema que pedirá as seguintes informações:

# Nome
# Idade
# Email
# Telefone

# apresentará o seguinte menu:

# Bem vindo(a)! <nome>

# Opções:

# 1 - Mostrar todas suas informações
# 2 - Mostrar apenas o seu nome e idade
# 3 - Mostrar seu email e telefone
# 0 - Sair

print('Bem Vindo!')
nome = input('Qual o seu nome?')
idade = int(input('Qual a sua idade?'))
email = input('Qual o seu email?')
telefone = input('Qual o seu telefone')

print(f'Bem vindo(a)!, {nome}')

while True:
    print('Escolha uma opção')
    print('1 - Mostrar todas suas informações')
    print('2 - Mostrar apenas o seu nome e idade')
    print('3 - Mostrar seu email e telefone')
    print('0 - Sair')
    opcao = int(input('>>> '))
    if opcao == 1:
        print(f'Seus dados completos são:\n Nome:{nome}\n \
            Idade:{idade}\n Email:{email}\n Telefone:{telefone}\n')
        input('Pressione enter para retornar as opções')
    elif opcao == 2:
        print(f'O nome informado foi {nome} e idade {idade}')
        input('Pressione enter para retornar as opções')
    elif opcao == 3:
        print(f' O e-mail informado foi {email} e telefone {telefone}') 
        input('Pressione enter para retornar as opções')
    elif opcao == 0:
        print('sair')
        break
    else:
        print('opção inválida!!') 
