# # import psycopg2

# # con = psycopg2._connect("host=localhost dbname=projeto user=admin password=4linux") 

# # cur = con.cursor()

# # cur.execute("insert into scripts(nome,conteudo) values ('teste.py', 'teste de conexão ao banco')")

# # con.commit()

# import psycopg2

# try:
#     con = psycopg2._connect("host=localhost dbname=projeto user=admin password=4linux") 

#     cur = con.cursor()

#     cur.execute("insert into scripts(nome,conteudo) values ('testetry.py', 'teste de try')")

#     con.commit()
# except Exception as e:
#     print('Erro: {}'.format(e))
#     print('Fazendo rollback')
#     con.rollback()

# finally:
#     print('Finalizando conexão com o banco')
#     cur.close()
#     con.close()


from pymongo import MongoClient

client = MongoClient('localhost')

db = client['dexterops']

def inserir_dados():
    try:
        db.fila.insert({"_id":1, "empresa":"4linux",
        "cursos": [{"nome":"Python Fundamentals",
                    "carga horaria":40},
                    
                  {"nome":"Linux Fundamentals",
                   "carga horaria":40}]})
    
    except Exception as e:
        print('erro: {}'.format(e))
