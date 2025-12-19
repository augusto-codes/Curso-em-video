'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
nota_50 = 0
nota_20 = 0
nota_10 = 0
nota_1 = 0

print(f'{'='*30}\n      SISTEMA DE CAIXA\n{'='*30}')

dinheiro = int(input('Digíte o valor que deseja retirar: '))
while True:
    if dinheiro >= 50:
        nota_50 += 1
        dinheiro -= 50
    elif dinheiro < 50 and dinheiro >= 20:
        nota_20 += 1
        dinheiro -= 20
    elif dinheiro < 20 and dinheiro >= 10:
        nota_10 += 1
        dinheiro -= 10
    elif dinheiro < 10 and dinheiro >= 1:
        nota_1 += 1
        dinheiro -= 1
    else:
        break
if nota_50 > 0:
    print(f'TOTAL DE {nota_50} DE R$50,00')
if nota_20 > 0:
    print(f'TOTAL DE {nota_20} DE R$20,00')
if nota_10 > 0:
    print(f'TOTAL DE {nota_10} DE R$10,00')
if nota_1 > 0:
    print(f'TOTAL DE {nota_1} DE R$1,00')
print('=' * 30)
print('VOLTE SEMPRE AO BANCO AUGUST')