m = 0

while m < 40 or m > 110:
    m = int(input('Insira a idade de Dona Mônica aqui: '))

a = 0
b = 0
while b == a or b < 1 or a < 1 or a > m or b > m:
    a = int(input('Insira a idade de um filho de Dona Mônica aqui: '));
    b = int(input('Insira a idade de outro filho de Dona Mônica aqui: '));

c = m - a - b

x = (a,b,c)

print('A idade do filho mais velho de Dona Mônica é: ' , max(x) )