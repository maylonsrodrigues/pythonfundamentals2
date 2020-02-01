print ('-------------------------------------------/n')
print ('Programa de folha de pagamento\n')

valorhora = float (input ('digite o valor da hora'))
qtdhora = float  (input ('digite a quantidade de horas trabalhadas'))

salariobruto = valorhora * qtdhora

print ('Salario bruto: ', salariobruto)

if salariobruto <= 1900: 
    salariobrutoir = salariobruto
    print('isento de IR')
elif salariobruto >= 1901 and salariobruto <= 2800:
    salariobrutoir = ((7/100) * salariobruto) 
    print('Faixa de desconto de 7% de IR, valor do desconto é ', salariobrutoir)
elif salariobruto >= 2801 and salariobruto <= 3700:
    salariobrutoir = ((15/ 100) * salariobruto) 
    print('Faixa de desconto de 15% de IR, valor do desconto é ', salariobrutoir)
elif salariobruto >= 3701 and salariobruto <= 4600:
    salariobrutoir = ((22 / 100) * salariobruto) 
    print('Faixa de desconto de 22% de IR, valor do desconto é ', salariobrutoir)
else:
    salariobruto >= 4601
    salariobrutoir = ((27/ 100) *  salariobruto) 
    print ('Faixa de desconto de 27% de IR, valor do desconto é ', salariobrutoir)


sind = (3 / 100) * salariobruto
print('Sindicato: ', sind)

fgts = (11 / 100) * salariobruto
print('FGTS: ', fgts)

totdesc = salariobrutoir + sind + fgts
print ('total de descontos ', totdesc)

salliquido = salariobrutoir - sind - fgts
print ('Salario liquido', salliquido)

print ('-------------------------------------------/n')