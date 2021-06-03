numeros = 0
listapar = []
listaimpar = []

for k in range(0, 21):
    f = int(input('Insira um numero aqui: '))
    if f % 2  == 0:
        listapar.append(f)
    else:
        listaimpar.append(f)

print(listapar)
print(listaimpar)