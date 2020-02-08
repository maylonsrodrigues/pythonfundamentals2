# print ('-------------------------------------------/n')
# print ('Programa de folha de pagamento\n')

# valorhora = float (input ('digite o valor da hora'))
# qtdhora = float  (input ('digite a quantidade de horas trabalhadas'))

# salariobruto = valorhora * qtdhora

# print ('Salario bruto: ', salariobruto)

# if salariobruto <= 1900: 
#     salariobrutoir = salariobruto
#     print('isento de IR')
# elif salariobruto >= 1901 and salariobruto <= 2800:
#     salariobrutoir = ((7/100) * salariobruto) 
#     print('Faixa de desconto de 7% de IR, valor do desconto é ', salariobrutoir)
# elif salariobruto >= 2801 and salariobruto <= 3700:
#     salariobrutoir = ((15/ 100) * salariobruto) 
#     print('Faixa de desconto de 15% de IR, valor do desconto é ', salariobrutoir)
# elif salariobruto >= 3701 and salariobruto <= 4600:
#     salariobrutoir = ((22 / 100) * salariobruto) 
#     print('Faixa de desconto de 22% de IR, valor do desconto é ', salariobrutoir)
# else:
#     salariobruto >= 4601
#     salariobrutoir = ((27/ 100) *  salariobruto) 
#     print ('Faixa de desconto de 27% de IR, valor do desconto é ', salariobrutoir)


# sind = (3 / 100) * salariobruto
# print('Sindicato: ', sind)

# fgts = (11 / 100) * salariobruto
# print('FGTS: ', fgts)

# totdesc = salariobrutoir + sind
# print ('total de descontos ', totdesc)

# salliquido = salariobruto - totdesc
# print ('Salario liquido', salliquido)

# print ('-------------------------------------------/n')

# -*- coding: utf-8 -*-

vlr_hora = float(input('Digite o valor da hora: '))
qtd_hora = float(input('Digite a quantidade de horas trabalhadas: '))

salario_bruto = (qtd_hora * vlr_hora)

if salario_bruto >= 4600:
    ir = 27
elif salario_bruto > 3700 and salario_bruto < 4600:
    ir = 22
elif salario_bruto > 2800 and salario_bruto <= 3700:
    ir = 15
elif salario_bruto > 1900 and salario_bruto <= 2800:
    ir = 7
else:
    ir = 0

valorIR = salario_bruto * (ir / 100.0)
valor_sindicato = salario_bruto * (3 / 100.0)
valorFGTS = salario_bruto * (11 / 100.0)
total_desconto = valorIR + valor_sindicato

salario_liquido = salario_bruto - total_desconto

print('\nSalario Bruto: ({} * {}): {}'.format(vlr_hora, qtd_hora, salario_bruto))
print('(-) IR ({})%: R${}'.format(ir, valorIR))
print('(-) Sindicato (3%): R${}'.format(valor_sindicato))
print('FGTS (11%): R${}'.format(valorFGTS))
print('Total de Descontos: R${}'.format(total_desconto))
print('Sálario Liquido: R${}'.format(salario_liquido))