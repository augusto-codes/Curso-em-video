'''Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''

primeiro_termo = int(input('Digíte o primeiro termo: '))
razao = int(input('Digíte a razão da PA: '))
contador = 0

while contador < 10:
    print(primeiro_termo, end=' -> ')
    primeiro_termo += razao
    contador = contador + 1
print('Fim')
