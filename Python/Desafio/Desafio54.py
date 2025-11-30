'''Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

Para deixar mais interassante, deixe como uma forma de cadastro'''
import datetime

hoje = datetime.datetime.now()
ano_atual = hoje.year

maior_idade = 0
menor_idade = 0

#Cores para o terminal
cor_vermelha = '\033[31m'
cor_verde = '\033[32m'
cor_padrao = '\033[m'
negrito = '\033[1;36m'

#Inicio
print('-=-' * 20)
print(f'{negrito}Vamos cadastrar pessoas!!!{cor_padrao}')
print('-=-' * 20)

numero_pessoas = int(input('Digíte o número de pessoas para cadastro: '))
lista_pessoas = []

for i in range(numero_pessoas):
    nome = input(f'Digíte o nome da pessoa número {i + 1}: ')
    lista_pessoas.append(nome)

lista_completa = {}
for pessoa in lista_pessoas:
    ano = int(input(f'Digíte o ano de nascimento de {pessoa}: '))
    lista_completa[pessoa] = ano

for nome_i, ano_i in lista_completa.items():
    if (ano_atual - ano_i) < 18:
        print(f'{cor_vermelha}{nome_i} tem {ano_atual - ano_i} anos, ainda é menor de idade{cor_padrao}')
        menor_idade = menor_idade + 1
    else:
        print(f'{cor_verde}{nome_i} tem {ano_atual - ano_i} anos, ele já é maior de idade{cor_padrao}')
        maior_idade = maior_idade + 1

print(f'Em {numero_pessoas} pessoa(s) tem com menoridade {cor_vermelha}{menor_idade}{cor_padrao} pessoa(s) e com maioridade tem {cor_verde}{maior_idade}{cor_padrao} pessoa(s).')



