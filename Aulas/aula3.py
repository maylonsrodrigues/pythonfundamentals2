# itens = []

# for item in range(1, 100):
#     itens.append(item)
# print (itens)

# carros = ['golf', 'fox', 'camaro']
# cores = ['branco', 'preto', 'azul']

# for carro in carros:
#     for cor in cores:
#         print (carro, cor)

# erros e exceções

# try:
#     if nome == 'renato':
#         print(nome)

# except Exception as e:
#     print('|erro: variavel nao existe')


# try:
#     nome = int (input('digite seu nome'))
#     if nome == 'renato':
#         print(nome)

# except NameError:
#     print('|erro: variavel nao existe')

# except ValueError:
#     print('o valor nao numeral') 

# except Exception: 
#     print('Exception')
# ========================================================
# try:
#     x = int(input('digite o primeiro valor'))
#     y = int(input('digite o segundo valor'))
# print(x + y)

# except ValueError: 
#      print('Digite apenas numeros')

# finally: 
#     print ('saindo do try/except')
# =========================================
# blacklist = ['daniel', 'camila']

# try:
#     nome = input('Digite o seu nome ')
#     print(nome)
#     if nome in blacklist:
#         raise NameError('usuario bloqueado')

# with open('arquivo.txt', 'w') as f:
#     f.write('arquivo texto')

# with open('arquivo2.txt', 'r+') as f:
#     f.write('arquivo texto 2444')

# try:
#    with open('arquivo.txt', 'r') as f:
#     print(f.read())
# except Exception:
#     print('erro')

# finally:
#     f.close()
