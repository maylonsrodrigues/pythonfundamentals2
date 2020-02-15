# class Carro():

#     def __init__(self):
#         self.rodas = 4 
#         self.motor = True

#     def ligar(self):
#         print('ligado...')

#     def remover_motor(self):
#         self.motor = False

# palio = Carro()
# palio.ligar()

# class servidor():

#     def __init__(self, servico, disco, processador, memoria):
#         self.servico = servico
#         self.disco = disco
#         self.processador = processador
#         self.memoria = memoria

#     def addMemoria(self, addM):
#         self.memoria += addM

#     def addArmazenamento(self, addD):
#         self.disco += addD
    
#     def mudaServico(self, new_service):
#         self.servico = 'new_service'


# servidorweb = servidor('Nginx', 250, 'i7 9gen', 16)
# print(servidorweb.servico)
# print(servidorweb.disco, 'GB')
# print(servidorweb.processador)
# print(servidorweb.memoria, 'GB')
# print ('?\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\?')

# servidorweb.addMemoria(8)
# servidorweb.addArmazenamento(120)
# servidorweb.mudaServico('iis')

# print(servidorweb.servico)
# print(servidorweb.disco, 'GB')
# print(servidorweb.processador)
# print(servidorweb.memoria, 'GB')
# print ('?\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\?')


#polimorfismo

# class servidor():

#     def __init__(self):
#         self.disco = 150
#         self.processador = 'xeon'
#         self.memoria = 16

#     def addMemoria(self, addM):
#         self.memoria += addM

#     def addArmazenamento(self, addD):
#         self.disco += addD
    
#     def mudaServico(self, new_service):
#         self.servico = 'new_service'

# class servidorweb(servidor):
#     def __init__(self):
#         super().__init__() #metodo busca atributos do pai
#         self.servico = 'nginx'
        

# class servidorEmail(servidor):
#     pass
    
# vader = servidorweb()

# print (vader.disco)

