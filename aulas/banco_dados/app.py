# # import sqlite3


# # #Criando a conexao com o banco
# # con = sqlite3.connect('banco.db')

# # #Criar um cursor para apontar onde manipular dados 
# # cursor = con.cursor() 

# # SQL_STRING = """
# # create table produto (
# #     id integer primary key autoincrement,
# #     nome text,
# #     desc text,
# #     preco real,
# #     ativo boolean
# # );
# # """
# # #tratmento de excecao no banco de dados
# # try:
# #     cursor.execute(SQL_STRING)
# #     con.commit()
# # except Exception as e:
# #     print(e)
# #     con.rollback()
# # finally:
# #     con.close()


# import psycopg2
# import getpass

# senha = getpass.getpass()
# conexao = psycopg2.connect(f'host=localhost dbname=projeto user=admin password={senha}')

# cursor = conexao.cursor()

# def insertUsuario():
#     nome = input('Digite o nome do usuario: ')
#     email = input('Degite o email: ')
#     endereco = input('digite o endereco: ')
#     try:
#         cursor.execute(f"insert into usuarios(nome,email,endereco) values ('{nome}', '{email}', '{endereco}');")
#         conexao.commit()
#         print ('Dados Inseridos')
#     except Exception as e:
#         print(f'ERRO:{e}')
#         conexao.rollback()
#     finally:
#         print('Conexao finalizada')


# def selectUsuario():
#     user_id = input('Id: ')
#     usuarios = cursor.execute(f'select * from usuarios where id={user_id};')
#     print(cursor.fetchall())

# def deleteUsuario():
#     user_id = input('Id: ')
#     usuarios = cursor.execute(f'delete from usuarios where id={user_id};')
#     print(cursor.fetchall())

# def updateUsuario():
#     pass

# #insertUsuario()
# #selectUsuario()
# deleteUsuario()
# #updateUsuario()


from pymongo import MongoClient 

client = MongoClient('localhost')
db = client['clientes']

def insertDocument():
    nome = input('Nome: ')
    idade = input ('idade: ')
    valorDivida = int(input('Valor da Divida: '))
    try:
        db.cadastro.insert_one({
            "nome": nome, 
            "idade": idade,
            "valorDivida": valorDivida
            })
    except Exception as e:
        print(e)


def findDocument():
    for document in db.clientes.find():
            print('============')
            print(document)

def deletDocument():
    pass

def updateDocument():
    pass
insertDocument()

