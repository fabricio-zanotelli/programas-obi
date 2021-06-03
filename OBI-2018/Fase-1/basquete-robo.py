distancia = -1
while distancia < 0 or distancia > 2000:
    distancia = int(input())

if distancia < 800:
    print(1)
elif distancia > 800 and distancia < 1400:
    print(2)
else:
    print(3)

