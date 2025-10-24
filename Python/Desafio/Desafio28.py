'''Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import choice
import time
print('-=-' * 20)
print('Vamos brincar de adivinhação!!!')
print('-=-' * 20)
num = input('Digíte um número de 0 a 5: ')
escolha = choice(['0','1','2','3','4','5'])
print('Processando...')
tempo = time.sleep(2)

if escolha == num:
    print(f'Parabéns!!! O número {num} que você escolheu também foi escolhido pelo sistema')
else:
    print(f'Tente novamente!! O número escolhido pelo sistema foi {escolha}')