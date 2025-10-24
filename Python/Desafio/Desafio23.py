'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''
'''Opção 1:
num = input('Digíte seu numero de 0 a 9999: ')
num1 = num.replace('',' ').split()
print(f'O número é {num1}')

for i in num1:
    print(i)'''

'''Opção 2:
num = int(input('Digíte seu número: '))
print(f"""Analisando seu número...
      Seu número é: {num}
Unidade: {num // 1 % 10}
Dezena: {num // 10 % 10}
Centena: {num // 100 % 10}
Milhar: {num // 1000 % 10}""")'''