# PROGRAMAS OBI
> Projeto de estudo visando a implementação de algorítimos diversificados que já foram questões das provas da OBI.

## Índice

- [Idade da Dona Mônica](#idade-da-dona-monica)
    - [Especificação](#especificação)
- [CARRO DA OBI](#carro-da-obi)
    - [Especificação](#especificação)
- [CAIXA DRONE](#caixa-drone)
    - [Especificação](#especificação)
									

## Idade da Dona Mônica

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
	
 
## CARRO DA OBI

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
	

#  CAIXA DRONE
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
