'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''
lado_a = float(input('Digíte o comprimento do lado A: ').replace(',','.'))
lado_b = float(input('Digíte o comprimento do lado B: ').replace(',','.'))
lado_c = float(input('Digíte o comprimento do lado C: ').replace(',','.'))

if (lado_a + lado_b) > lado_c and (lado_a + lado_c) > lado_b and (lado_b + lado_c) > lado_a:
    print('\033[32mÉ possivel montar um triângulo com suas medidas\033[m')
else:
    print('\033[31mNão é possivel montar um triângulo com suas medidas\033[m')
