'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''
from datetime import date

ano = int(input('Que ano gostaria de analisar? Coloque 0 para atualizar o ano atual: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é um ano bissexto')
else:
    print(f'O ano de {ano} não é um ano bissexto')