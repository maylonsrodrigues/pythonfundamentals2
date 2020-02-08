# produtos = []

# def cadastraProduto(produto):
#     global produtos
#     produtos.append(produto)

# def listarProdutos():
#     global produtos
#     print (produtos)

# def deletaProduto():
#     global produtos
#     produtos.remove(produto)

# cadastraProduto('batata')
# cadastraProduto('laranja')
# cadastraProduto('abacaxi')
# listarProdutos()
# deletaProduto('laranja')

#crie funções que receba x e y e retorne a soma, subtracao


# def soma(x, y):
#     return x + y
#     soma(10, 15)

# def sub (x, y):
#     return x - y
#     sub(10 , 5)

# print (soma (10, 5))
# print (sub (10, 5))

#faca uma função que recebe 2 valores como parametro e imprime o maior 

# def maior(n1, n2):
#    print(max(n1, n2))

# maior(n3, n4)
##################################################################
# def ordenavalores(*valores):
#     print(sorted(valores))

# ordenavalores(1, 2, 3, 4, 90, 80, 50, 100, 101)
#################################################################
# def ordenavalores(*valores):
#     return sorted(valores)

# l= ordenavalores(1, 2, 3, 4, 90, 80, 50, 100, 101)

# print (l)
# print(max(l))
################################################################

# import requests

# def api(**valores):
#     req = requests.get(valores['URL'])
#     print(valores)
#     return req

# print (api(URL= 'https://google.com.br', code_status= 200, retorno='ok'))

#################################################################

# sub2 = lambda x, y: x - y

# sub2(10, 5)

# lista = [1,3,3,4,5,6,7,8,9]

# dobro = list(map(lambda x: x*2, lista ))

# print(dobro)

#

# from functools import reduce

# soma = reduce((lambda x, y: x + y), [1,3,3,4,5,6,7,8,9])

# print (soma)

# lista = [1,3,3,4,5,6,7,8,9, 45,68,89,0]

# n_par= list(filter(lambda x: x % 2 == 0, lista)) 

# print(n_par)