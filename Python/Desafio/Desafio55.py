'''Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''
maior_peso = 0
maior_peso_pessoa = 0
menor_peso = 1000
menor_peso_pessoa = 0
for i in range(5):
    peso = float(input(f'Digíte o peso da pessoa número {i + 1}: ').replace(',','.'))
    if peso > maior_peso:
        maior_peso = peso
        maior_peso_pessoa = i + 1

    elif peso < menor_peso:
        menor_peso = peso
        menor_peso_pessoa = i + 1

print(f'A pessoa com o maior peso foi a de número {maior_peso_pessoa}, pesando {maior_peso}Kg')
print(f'A pessoa com o menor peso foi a de número {menor_peso_pessoa}, pesando {menor_peso}Kg')



