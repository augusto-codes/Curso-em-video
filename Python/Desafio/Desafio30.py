'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''
print('Descubra se o número escolhido é ímpar ou par')
num = int(input('Digíte um número inteiro: '))
resto = (num % 2)
if resto > 0:
    print(f'O número {num} é ímpar')
else:
    print(f'O número {num} é par')