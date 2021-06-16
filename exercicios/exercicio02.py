# Criar uma aplicação de Calculo de média


# Entradas:
    # nome do aluno
    # n1 - nota número 01
    # n2 - nota número 02
    # n3 - nota número 03
    # n4 - nota número 04
# Saída:
    # Retornar a média do aluno no formato:
    
    # Nome do aluno
    # Nota final

    # Retornar resultado do aluno:

    # se o aluno obteve média acima de 7 -> Aprovado
    # se o aluno obteve média acima de 6 ->  e abaixo de 7 -> Recuperação
    # se o aluno obteve média abaixo de 6 -> Reprovado

aluno = input ("Digite o Nome do Aluno: ") 
n1= float(input("Digite e nota numero 1: "))  
n2= float(input("Digite e nota numero 2: ")) 
n3= float(input("Digite e nota numero 3: ")) 
n4= float(input("Digite e nota numero 4: "))

media = (n1 + n2 + n3 + n4)/4

if media >= 7:
    print(f'Parabéns {aluno}, você foi aprovado!')

elif media >= 6:
    print(f'{aluno}, vocẽ ficou de recuperação!')
    
else:
    print ('Você foi reprovado!')
