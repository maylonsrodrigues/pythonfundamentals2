# var = str (input('digite um valor'))

# texto = 'esse texto é texto'

# # texto.upper()
# # #split print (texto.slip(''))
# # texto.captalize()
# # texto.lower()

# lista = ['abacaxi', 'banana', 'maça', 1, 2, 3]

# print (lista[3])

# #ista.append []
# #lista.pop(0)
# #lista.remove()
# #lista.sort()

# # tupla
# valor1 = (0, 1, 2, 3)
# valores = (0, 1, 2, [1, 3, 4], {'chave': 'valor'})

# print (valores)


# #dicionarios

# ling_favorita = {'joao' : 'java', 'daniel': 'python', 'hector' : 'php'}

# print (ling_favorita['daniel'])

# time_favorito = {'joao' : 'corinthians', 'rafael' : 'vasco', 'camila' : 'palmeiras'}

# print (time_favorito ['camila'])

# #modificar dados do dicionario
# time_favorito ['rafael'] = 'flamengo'
# print (time_favorito)
# #printar valores e chaves
# print (time_favorito.values())
# print (time_favorito.keys())

# #

# dados_clientes = {'cliente': {'cl001' : {'nome': 'Rafael da silva', 'idade': 25, 'telefone' : '01196969696'},
#                               'cl002' : {'nome': 'clara pereira', 'idade' : 28, 'telefone' : '012969693'}}}

# print (dados_clientes ['cliente'])
# print (dados_clientes ['cliente']['cl002'])
# print (dados_clientes ['cliente']['cl002']['nome'])
# # print (dados_clientes ['cliente']['cl002']['nome'], dados_clientes['cliente']['cl002']['idade']

# update de informação no dicionario

# dados_clientes ['cliente']['cl002']['telefone'] = 'xxxxxxxx'

# print (dados_clientes ['cliente']['cl002'])

# imprime_clientename = input('digite o codigo do cliente: ')

# print (dados_clientes ['cliente'][imprime_clientename])

idade = int (input('digite sua idade '))
habilitacao =  int (input('Possui Habilitação:\n 1- para Sim ou \n2- para Nao\n  '))

if idade >= 18 and habilitacao == 1:
    print ('voce pode dirigir')
else:
    print ('voce nao pode dirigir')

