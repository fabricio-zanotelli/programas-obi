numnat = -1
while numnat < 0 or numnat > 100:
    numnat = int(input('O maior numero de circulos em um dos lados da peça do seu jogo de domino é: '))

numpec = ((numnat + 1) * (numnat + 2))/2

print('Esse jogo tem ' + numpec.__str__() + ' peças')