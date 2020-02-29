from sqlalchemy import update
from core import user_table, engine

con = engine.connect()

def atualizar_nome(nome_antigo, novo_nome):
    atualizar = update(user_table).where(user_table.c.nome == nome_antigo)
    atualizar = atualizar.values(nome = novo_nome)
    result = con.execute(atualizar)
    print(result.rowcount)

atualizar_nome('thiago', 'Ricardo')