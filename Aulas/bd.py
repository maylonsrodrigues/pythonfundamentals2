from pymongo import MongoClient

client = MongoClient('localhost')

db = client['dexterops']

def buscar_dados():
    for r in db.fila.find():
        print('Empresa: {}'.format(r['empresa']))
        for c in r['cursos']:
            print(20*'=')
            print('Nome: {} \n Carga Horaria: {}'.format(c['nome'], c['carga horaria']))



def update_instrutor():
    db.fila.update({"id": 1,"instrutores.nome": "Mariana"},
    {"$set":{"instrutores.$.nome": "Marcia"}})

    update_instrutor()

def update_email():
    db.fila.update({"_id": 1, "instrutores.nomes": "Marcia"},
    {"$set":{"instrutores.$.email": "marcia@4linux.com.br"}})

    update_email():