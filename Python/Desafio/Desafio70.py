'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

#Criando as info necessario
total_gasto = 0
acima_mil = 0
menor_valor = 10000
lista = []

#Loop para cadastro
while True:
    nome_produto = input('Digíte o nome do produto: ').strip().upper()
    valor_produto = float(input('Digíte o valor do produto: R$').replace(',','.'))
    lista.append((nome_produto, valor_produto))
    pergunta = input('Deseja contiuar? [S/N] ').upper()
    print('=' * 40)
    if pergunta == 'N':
        break

#Tratamento de dados
for i in lista:
    nome, valor = i
    total_gasto += valor
    if valor > 1000:
        acima_mil += 1
    if valor < menor_valor:
        item_barato = nome
        menor_valor = valor

#Mostrando valores
print(f'O total gasto na compra foi de R${total_gasto:.2f}\nNesta compra teve {acima_mil} itens que custou mais de R$1000,00\nO item mais barato foi o {item_barato:.2f} e custava R${menor_valor}')