# # Strings - Conjunto de caracteres


# # Métodos de string

# nome = input("Qual é o seu nome? ")

# texto = "{}, seja bem vindo(a)".format(nome)

# dividindoTexto = texto.split('a')
# caixaBaixa = texto.lower()
# caixaAlta = texto.upper()
# texto.endswith("!")
# texto.startswith('Olá')
# texto.strip('a')
# texto.capitalize
# print(texto.count('a'))


# # # Indexação de String
# texto2 = "Apenas uma String qualquer"
# print(texto2[:6])
# print(texto2[6:])
# print(texto2[5:10])
# print(texto2[:])
# print(texto2[::])
# print(texto2[::2])


# Estrutura Condicional

# nome = input('Digite seu nome: ')
# idade = int(input('Digite sua idade: '))
# habilitacao = input('Possui habilitação? (s/n)')
# credito = False

# # SE
# if idade >= 18 and habilitacao == 's' and credito == True:
# 	print(f'Bem vindo(a) {nome}!')
# 	print('Você pode alugar um carro!')

# # SE NÃO, SE
# elif idade >= 18 and habilitacao == 's':
# 	print(f'Bem vindo(a) {nome}!')
# 	print('Você pode alugar um carro, apenas com pagamento adiantado')

# # SE NÃO
# else:
# 	print(f'Bem vindo(a) {nome}!')
# 	print('Infelizmente, você não pode alugar um carro')
