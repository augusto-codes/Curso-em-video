'''Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.'''
from random import choice
import time

cor_amarela = "\033[33m"
cor_vermelha = '\033[31m'
cor_verde = '\033[32m'
cor_padrao = '\033[m'
negrito = '\033[1;36m'

print(f'{cor_amarela}-=-{cor_padrao}' * 30)
print(f'{negrito}Vamos jogar jokenpô{cor_padrao}')
print(f'{cor_amarela}-=-{cor_padrao}' * 30)

usuario = int(input('''Esolha...
1 - Pedra
2 - Papel
3 - Tesoura

Digíte sua escolha: '''))

maquina = choice([1, 2, 3])

if usuario == maquina:
    print(f'Empatamos, ambas escolhas foram {maquina}!!')
elif usuario == 1 and maquina == 3:
    print(f'{cor_verde}Parabéns, você me venceu!! sua escolha foi pedra e a minha foi tesoura {cor_padrao}')
elif usuario == 2 and maquina == 1:
    print(f'{cor_verde}Parabéns, você me venceu!! sua escolha foi papel e a minha foi pedra {cor_padrao}')
elif usuario == 3 and maquina == 2:
    print(f'{cor_verde}Parabéns, você me venceu!! sua escolha foi tesoura e a minha foi papel {cor_padrao}')
else:
    print(f'{cor_vermelha}Hahaha, você perdeu!!! Eu escolhi {maquina} já você {usuario}, {negrito}perdedor!!!{cor_padrao}')
