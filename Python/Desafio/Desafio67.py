'''Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''
cont = 0
n = int(input(f'{'=' * 30}\nQuer ver qual valor de tabuada? '))
print('=' * 30)

while True:
    if cont > 10:
        n = int(input(f'{'=' * 30}\nQuer ver qual valor de tabuada? '))
        print('=' * 30)
        cont = 0
    else:
        print(f'{n} x {cont} = {n * cont}')
        cont += 1
    if n < 0:
        break
print('Obrigado por usar nossa tabuada')