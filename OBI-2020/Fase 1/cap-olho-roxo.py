tripulacao = 0
ouro = 0

#while tripulacao < 1 or tripulacao > 1000 or ouro < 3 or ouro > 1000 or tripulacao > ouro:
#    tripulacao = int(input())
#    ouro = int(input())
#
#ouroTripulacao = ouro / (tripulacao +2)
#ouroCapitao = ouroTripulacao * 2

#print(ouroCapitao)

while tripulacao < 1 or tripulacao > 1000 or ouro < 3 or ouro > 1000 or tripulacao > ouro:
   tripulacao = int(input('Tripulacao: '))
   ouro = int(input())

ouroTripulacao = ouro / (tripulacao +2)
ouroCapitao = ouroTripulacao * 2

print(ouroCapitao)

