
restricao = True

while restricao:
    c_1 = int(input("Caixa 1: "))
    c_2 = int(input("Caixa 2: "))
    c_3 = int(input("Caixa 3: "))
    restricao = (c_1 < 1) or (c_1 > c_2) or (c_2 > c_3) or (c_3 > 1000)

def checkIgual(valor1, valor2):
    if valor1 != valor2:
        return 1
    else:
        return 0

viagens = 3 - checkIgual(c_1, c_2) - checkIgual(c_2, c_3)

print(viagens.__str__() + "  Serão necessárias")
