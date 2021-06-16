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
    
aluno = input ("Digite o Nome do Aluno: ") 
n1= float(input("Digite e nota numero 1: "))  
n2= float(input("Digite e nota numero 2: ")) 
n3= float(input("Digite e nota numero 3: ")) 
n4= float(input("Digite e nota numero 4: "))

media = (n1 + n2 + n3 + n4)/4

# print("A média do", aluno, "é ", media)
# print("A média do" {} "é" {}.format (aluno, media)
print(f"A média do {aluno} é {media}")  

