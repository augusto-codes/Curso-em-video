'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120
'''

num = int(input('Digíte o número que sera fatorado: '))
contator = num

print(f'Calculando {num}! ', end='')
while contator > 0:
    print(f'{contator}', end= '')
    print(' x ' if contator > 1 else ' = ', end='')
    contator = contator - 1
    if contator != 0:
        num = num * contator
print(num)