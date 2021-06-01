caixaaa = 0
caixabe = 0
caixace = 0

while caixaaa < 1 or caixaaa > caixabe or caixabe > caixace or caixace >1000:
    caixaaa = int(input('O tamanho da caixa A é de:'))
    caixabe = int(input('O tamanho da caixa B é de:'))
    caixace = int(input('O tamanho da caixa C é de:'))


if caixaaa < caixabe:
    if caixace == caixabe:
        print('Será necessário apenas duas viagens!')
    elif caixace > caixabe:
        print('Será necessário apenas uma viagem!')    
elif caixaaa == caixabe:
    if caixaaa + caixabe < caixace:
        print('Será necessário apenas uma viagens!')
    elif caixace == caixabe:
        print('Será necessário três viagens!')
    elif caixaaa or caixabe < caixace:
        print('Será necessário apenas duas viagens!')
elif caixabe < caixace:
    if caixaaa < caixabe:
        print('Será necessário apenas uma viagem!')
    else:
        if caixaaa + caixabe < caixace:
            print('Será necessario apenas uma viagem!')
        elif caixaaa == caixabe and caixabe == caixace:
            print('Será necessário três viagens!')
        else:
            print('Será necessário apenas duas viagens!')
elif caixaaa == caixabe and caixabe == caixace:
    print('Será necessário três viagens')
print('.')
