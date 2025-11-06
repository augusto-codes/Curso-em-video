'''Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''

positivo_cor = '\033[1;32m'
negativo_cor = '\033[1;31m'
padrao_cor = '\033[m'

#Recebendo informações do usuário
lado_a = float(input('Digíte o valor do lado A: ').replace(',','.'))
lado_b = float(input('Digíte o valor do lado B: ').replace(',','.'))
lado_c = float(input('Digíte o valor do lado B ').replace(',','.'))

#Validando se é possivel forma um triangulo com as informações do usuário
if (lado_a + lado_b) > lado_c and (lado_a + lado_c) > lado_b and (lado_b + lado_c) > lado_a:
    print(f'{positivo_cor}As medidas digítas formam um triângulo{padrao_cor}')
    if lado_a == lado_b and lado_a == lado_c and lado_b == lado_c:
        print('Pelas medidas apresentadas é um triângulo equilátero, já que todos os lados são iguais')
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        print('Pelas medidas apresentadas é um triângulo isósceles, já que possui dois lados iguais')
    else:
        print('Pelas medidas apresentadas é um triângulo escaleno, já que não possui lados iguais')
else:
    print(f'{negativo_cor}Suas medidas não formam um triângulo {padrao_cor}')