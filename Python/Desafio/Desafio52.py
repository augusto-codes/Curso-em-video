'''Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
cor_vermelha = '\033[31m'
cor_verde = '\033[32m'
cor_padrao = '\033[m'

print('-=-' * 20)
print('Verificando se o número é primo')
print('-=-' * 20)

numero = int(input('Digíte o número que deseja validar: '))

contador = 0
for c in range(1, numero + 1):
    if (numero % c) == 0:
        print(f'O número {numero} foi divido por {c}')
        contador = contador + 1

if contador == 2:
    print(f'{cor_verde}O número {numero} é primo, teve apenas {contador} divisores{cor_padrao}')
else:
    print(f'{cor_vermelha}O número {numero} não é primo, ele teve {contador} divisores{cor_padrao}')