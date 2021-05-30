carroaa = -1
carrobe = 0
carroce = 0

while carroaa < 0 or carrobe < carroaa or carrobe > carroce or carroce > 500:
    carroaa = int(input('A posição da traseira do carro A é de: '))
    carrobe = int(input('A posição da traseira do carro B é de: '))
    carroce = int(input('A posição da traseira do carro C é de: '))

distanciaaabe = carrobe - carroaa
distanciabece = carroce - carrobe

if distanciaaabe < distanciabece:
    print(1)

elif distanciabece < distanciaaabe:
    print(-1)

else:
    print(0)