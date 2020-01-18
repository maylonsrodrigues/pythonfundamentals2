# #faça um programa que receba 4 notas de alunos 
# # some e divida por 4

# print(':....programa recebe notas e divide por 4....:')

# n1 = float (input('digite a nota do 1 aluno:_ '))
# n2 = float (input('digite a nota do 2 aluno:_ '))
# n3 = float (input('digite a nota do 3 aluno:_ '))
# n4 = float (input('digite a nota do 4 aluno:_ '))
# soma = (n1 + n2 + n3 + n4)
# print (soma, 'é o total das notas...')
# divi = (soma / 4 )
# print (divi, 'é o total das notas dividido por 4...')
# print ('<<<The end>>>')

lista = ['Corinthians', [1, 2, 3, 4, 5] ,'Palmeiras', 'São Paulo', [10, 11, 12, 13, 14],'Flamengo', 'Vasco']

# # print 3, 13, vasco
# print (lista[1][2], lista[4][3], lista[-1])
# #print 4, São Paulo, 14
# print (lista[1][-2], lista[3], lista[4][-1])
# # print Corinthians, 2, 10, 14
# print (lista[0], lista[1][1], lista[4][4], lista[4][-1])

lista.append('bragantino')jb.
lista.insert(0, 'sport')
lista.remove('Vasco')
lista.pop(0)


print(lista[:])
print(lista[3])

lista2 = ['c', 'd', 'a', 'b']
lista2.sort()
print(lista2)
