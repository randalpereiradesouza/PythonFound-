import sqlite3


#Criando a conexao com o banco
con = sqlite3.connect('banco.db')

#Criar um cursor para apontar onde manipular dados 
cursos = con.cursor() 

SQL_STRING = """
create table produto (
    id integer primary key autoincrement,
    nome text,
    desc text,
    preco real,
    ativo boolean
);
"""
#tratmento de excecao no banco de dados
try:
    cursos.execute(SQL_STRING)
    con.commit()
except Exception as e:
    print(e)
    con.rollback()
finally:
    con.close()