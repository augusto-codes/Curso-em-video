'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira
Ex: Digíte o número: 6,127
O número 6,127 tem a parte inteira 6.'''

#import math
from math import trunc , floor
num_real = input('Digíte o número: ').replace(',','.')
num_real = float(num_real)
#Opção1: print(f'O número {num_real} tem a parte inteira {math.trunc(num_real)}')
#Opção2: print(f'O número {num_real} tem a parte inteira {trunc(num_real)}')
#Opção3: print(f'O número {num_real} tem a parte inteira {(num_real - 0.50):.0f}') #SÓ FUNCIONA SE O NÚMERO FOR ARRENDODAR PARA BAIXO
#Opção4: print(f'O número {num_real} tem a parte inteira {math.floor(num_real)}')
#Opção5: print(f'O número {num_real} tem a parte inteira {floor(num_real)}')
#Opção6: print(f'O número {num_real} tem a parte inteira {int(num_real)}')