<<<<<<< HEAD
# PROGRAMAS OBI #
Algoritmos de resolução da OBI em python, as variaveis podem estar diferentes do que eles pede,
# Idade da Dona Mônica (idade-dona-monica.py)
=======
# PROGRAMAS OBI
> Projeto de estudo visando a implementação de algorítimos diversificados que já foram questões das provas da OBI.

## Índice

- [Idade da Dona Mônica](#idade-da-dona-monica)
- [CARRO DA OBI](#carro-da-obi)
- [CAIXA DRONE](#caixa-drone)
									

## Idade da Dona Mônica
>>>>>>> fadc0a8a5cd31d136af9832465fde1103e8974ca

Este é um projeto teste, desenvolvido em Python, para resolver uma questão da primeira fase da OBI 2019.

## Especificação:

Dona Mônica é mãe de três filhos que têm idades diferentes. Ela notou que, neste ano, a soma das idades dos seus três filhos é igual à idade dela. Neste problema, dada a idade de dona Mônica e as idades de dois dos filhos, seu programa deve computar e imprimir a idade do filho mais velho.

Por exemplo, se sabemos que dona Mônica tem 52 anos e as idades conhecidas de dois dos filhos são 14 e 18 anos, então a idade do outro filho, que não era conhecida, tem que ser 20 anos, pois a soma das três idades tem que ser 52. Portanto, a idade do filho mais velho é 20. Em mais um exemplo, se dona Mônica tem 47 anos e as idades de dois dos filhos são 21 e 9 anos, então o outro filho tem que ter 17 anos e, portanto, a idade do filho mais velho é 21.

### Entrada

A primeira linha da entrada contém um inteiro M representando a idade de dona Mônica. A segunda linha da entrada contém um inteiro A representando a idade de um dos filhos. A terceira linha da entrada contém um inteiro B representando a idade de outro filho.

### Saída

Seu programa deve imprimir uma linha, contendo um número inteiro, representando a idade do filho mais velho de dona Mônica.
Restrições
40 ≤ M ≤ 110
1 ≤ A < M
1 ≤ B < M
A ≠ B

### Exemplos
#### Entrada
- 52
- 14
- 18

#### Saída
-> 20
	
 
<<<<<<< HEAD
# PILOTO AUTOMATICO (carro-obi.py)
=======
## CARRO DA OBI
>>>>>>> fadc0a8a5cd31d136af9832465fde1103e8974ca

Algoritmo feito em Python para a questão ''PIloto automático'' da OBI 2019


 Uma grande fábrica de carros elétricos está realizando melhorias no sistema de piloto automático e precisa da sua ajuda para implementar um programa que decida se um carro B, que está trafegando no meio de dois carros A e C, precisa acelerar, desacelerar ou manter a velocidade atual. Os carros são iguais e os sensores do piloto automático vão fornecer, como entrada, a posição atual da traseira dos três carros. Veja um exemplo na figura.

O carro B precisa ser acelerado se a distância da sua traseira para a traseira do carro A for menor do que a distância da sua traseira para a traseira do carro C. Se for maior, ele precisa ser desacelerado. Se for igual, precisa manter a velocidade atual. Quer dizer, o carro B precisa ser acelerado se (B-A) < (C-B), desacelerado se (B-A) > (C-B) e manter a velocidade se (B-A) for igual a (C-B).

## Entrada

A primeira linha da entrada contém um inteiro A. A segunda linha da entrada contém um inteiro B. A terceira linha da entrada contém um inteiro C. Os três inteiros representam as posições atuais das traseiras dos carros A, B e C, respectivamente.

## Saída

Seu programa deve imprimir uma linha contendo um inteiro: 1 se o carro B precisa acelerar; -1 se precisa desacelerar; ou 0 se precisa manter a velocidade atual.

## Restrições

    0 ≤ A < B < C ≤ 500 

## Exemplos

Entrada

- 10
- 23
- 38

Saída

1
	

#  ENTREGA DE CAIXAS (caixa-drone.py)
Algoritmo feito em python para a resolução do problema 'entrega de caixas' da OBI 2020


Você precisa transportar três caixas vazias usando um drone que pode levantar uma caixa por vez apenas em cada viagem. Quer dizer, sempre dá para transportar as três caixas vazias fazendo três viagens do drone. Mas talvez dê para fazer menos do que três viagens, se for possível colocar uma caixa dentro de outra. As caixas têm formato de cubo e a única restrição para uma caixa ser colocada dentro de outra é o tamanho, não importando o peso.

Uma caixa de tamanho X pode ser colocada dentro de uma caixa de tamanho Y se X < Y. Note, portanto, que uma caixa não cabe dentro de outra do mesmo tamanho. Além disso, duas caixas de tamanhos X e Y podem ser colocadas, lado a lado, dentro de uma caixa de tamanho Z se (X+Y) < Z.

A figura ilustra as quatro configurações possíveis para o drone fazer uma viagem.

Neste problema, os tamanhos das três caixas são dados em ordem crescente e seu programa deve computar o número mínimo de viagens que o drone pode fazer para transportar todas as três caixas.

## Entrada

A primeira linha da entrada contém um inteiro A. A segunda linha da entrada contém um inteiro B. A terceira linha da entrada contém um inteiro C. Os três inteiros representam os tamanhos das três caixas.
Saída

Seu programa deve imprimir uma linha contendo um inteiro, representando o número mínimo de viagens que o drone pode fazer para transportar todas as três caixas.

## Restrições

    1 ≤ A ≤ B ≤ C ≤ 1000 

## Exemplos
Entrada

12
45
188

	Saída

1
<<<<<<< HEAD

# DIVISAO DO TESOURO (cap-olho-roxo.py)
Algoritmo feito em python para o problema da OBI 2020 'Divisão do tesouro'

order:2

O Capitão Olho Roxo e seus marinheiros encontraram uma arca com uma grande quantidade de moedas de ouro idênticas. Para a divisão das moedas, todos concordaram com a seguinte sugestão do Capitão:

    cada marinheiro exceto o Capitão deveria receber exatamente o mesmo número de moedas; e
    o Capitão deveria receber o dobro de moedas que um marinheiro recebe. 

Pode ser que o fato de o Capitão ser o único com uma pistola a bordo tenha contribuído para a concordância de todos, mas também contribuiu o fato de que na forma proposta a divisão era perfeita, não sobrando ou faltando moedas.

Dados o número de moedas na arca e o número de marinheiros, escreva um programa para determinar quantas moedas o Capitão Olho Roxo recebeu.

## Entrada

A primeira linha da entrada contém um número inteiro A, o número de moedas na arca. A segunda linha contém um inteiro N, o número de marinheiros (não contando o Capitão).

## Saída

Seu programa deve produzir na saída uma única linha, contendo um único inteiro, o número de moedas que o Capitão Olho Roxo deve receber.

## Restrições

    3 ≤ A ≤ 10000
    1 ≤ N ≤ 1000 

## Exemplos
Entrada

221
11

	Saída

34
	

 
Entrada

1000
8

	Saída

200
	

 
Entrada

3
1

	Saída

2
	

# RELOGIO DE ATLETA (relogio-atleta-OBI.py)

Algoritmo em python para a resolução do problema relogio de atleta da OBI 2020

order:1

Uma empresa está desenvolvendo um novo relógio eletrônico para atletas de alto desempenho. Uma das funcionalidades do novo relógio é que ele vai medir a frequência cardíaca atual (batidas do coração por minuto) e a capacidade de oxigenação atual do atleta. O relógio também vai calcular e armazenar a frequência cardíaca em repouso do atleta.

Os projetistas querem que o relógio emita um aviso para o atleta de que ele ou ela deve:

    diminuir o ritmo do exercício se a frequência cardíaca atual é maior do que três vezes a frequência cardíaca em repouso ou a capacidade de oxigenação atual é menor do que 95;
    aumentar o ritmo do exercício se a frequência cardíaca atual é menor do que duas vezes frequência cardíaca em repouso e a capacidade de oxigenação atual é maior do que 97;
    manter o ritmo de exercício se nenhuma das condições anteriores ocorrer. 

Dadas a frequência cardíaca em repouso, a frequência cardíaca atual e a capacidade de oxigenação atual obtidas pelo relógio, escreva um programa que produza a sugestão que o relógio deve emitir.

## Entrada

A entrada é composta por três linhas, cada uma contendo um único número inteiro. A primeira linha contém o inteiro R, a frequência cardíaca em repouso do atleta. A segunda linha contém o inteiro F, a frequência cardíaca atual do atleta. A terceira linha contém o inteiro C, a capacidade de oxigenação atual do atleta.

## Saída

Seu programa deve produzir uma única linha, contendo uma única palavra, em letras minúsculas, que deve ser 'aumentar', 'diminuir', ou 'manter', de acordo com os critérios estabelecidos acima. }

## Restrições

    35 ≤ R ≤ 100
    35 ≤ F ≤ 200
    50 ≤ C ≤ 100 

## Exemplos
Entrada

60
119
98

	Saída

aumentar
	

 
Entrada

60
190
100

	Saída

diminuir
	

 
Entrada

50
100
95

	Saída

manter
	

 
Entrada

50
100
94

	Saída

diminuir
	
# DOMINO (domino-OBI.py)

O jogo de dominó tradicional, conhecido como duplo-6, possui 28 peças. Cada peça está dividida em dois quadrados e dentro de cada quadrado há entre 0 e 6 círculos. O jogo é chamado de duplo-6 justamente porque esse é o maior número de círculos que aparece num quadrado de uma peça. A figura ao lado mostra uma forma de organizar as 28 peças do jogo duplo-6 em 7 linhas. Essa figura permite ver claramente quantas peças haveria num jogo de dominó, por exemplo, do tipo duplo-4: seriam todas as peças das 5 primeiras linhas, 15 peças no total. Também poderíamos ver, seguindo o padrão da figura, quantas peças possui o jogo de dominó conhecido como mexicano, que é o duplo-12. Seriam 91 peças, correspondendo a 13 linhas.

Para a nossa sorte, existe uma fórmula com a qual podemos calcular facilmente o número de peças de um jogo do tipo duplo-N, para um número N natural qualquer: ((N+1)*(N+2))/2. Neste problema, estamos precisando da sua ajuda para escrever um programa que, dado o valor N, use esta fórmula para calcular e imprimir quantas peças existem num jogo de dominó do tipo duplo-N.

## Entrada
A primeira linha da entrada contém um número natural N representando o tipo do jogo de dominó: duplo-N.

## Saída
Seu programa deve imprimir uma linha contendo um número natural representando quantas peças existem num jogo de dominó do tipo duplo-N.
Restrições

    0 ≤ N ≤ 10000 

## Exemplos
Entrada

6

	Saída

28
	

 
Entrada

12

	Saída

91
	

 


# BASQUETE DE ROBOS (basquete-robos.py)
Algoritmo feito em python para a resolução do problema 'basquete de robos' da OBI 2018

A organização da OIBR, Olimpíada Internacional de Basquete de Robô, está começando a ter problemas com dois times: os Bit Warriors e os Byte Bulls. É que os robôs desses times acertam quase todos os lançamentos, de qualquer posição na quadra! Pensando bem, o jogo de basquete ficaria mesmo sem graça se jogadores conseguissem acertar qualquer lançamento, não é mesmo? Uma das medidas que a OIBR está implantando é uma nova pontuação para os lançamentos, de acordo com a distância do robô para o início da quadra. A quadra tem 2000 centímetros de comprimento, como na figura.

Dada a distância D do robô até o início da quadra, onde está a cesta, a regra é a seguinte:

    Se D ≤ 800, a cesta vale 1 ponto;
    Se 800 < D ≤ 1400, a cesta vale 2 pontos;
    Se 1400 < D ≤ 2000, a cesta vale 3 pontos. 

A organização da OIBR precisa de ajuda para automatizar o placar do jogo. Dado o valor da distância D, você deve escrever um programa para calcular o número de pontos do lançamento.

## Entrada
A primeira e única linha da entrada contém um inteiro D indicando a distância do robô para o início da quadra, em centímetros, no momento do lançamento.

## Saída
Seu programa deve produzir uma única linha, contendo um inteiro, 1, 2 ou 3, indicando a pontuação do lançamento.

## Restrições

    0 ≤ D ≤ 2000 

## Exemplos

Entrada

1720

	Saída

3
	

 
Entrada

250

	Saída

1
	

 
Entrada

1400

	Saída

2
	
=======
>>>>>>> fadc0a8a5cd31d136af9832465fde1103e8974ca
