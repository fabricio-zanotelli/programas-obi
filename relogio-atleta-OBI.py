cardrepouso = 0
cardeuso = 0
oxi = 0

while cardrepouso < 35 or cardrepouso > 100 or cardeuso < 25 or cardeuso > 200 or oxi < 50 or oxi > 100:
    cardrepouso = int(input('A frequência cardiaca em repouso do atleta é de:'))
    cardeuso = int(input('A frequência cardiaca atual do atleta é de: '))
    oxi = int(input('a capacidade de oxigênação atual do atleta é de: '))

if cardeuso > cardrepouso*3 or oxi < 95:
    print('DIMINUIR')
elif cardeuso < cardrepouso * 2 and oxi > 97:
    print('AUMENTAR')
else:
    print('MANTER')