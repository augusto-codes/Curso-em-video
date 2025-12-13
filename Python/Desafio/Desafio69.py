'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''
lista = []
cont = 1
soma_idade = 0
soma_homem = 0
soma_mulher = 0
while True:
    nome = input(f'Digíte o nome da {cont}º pessoa: ').upper().strip()
    sexo = input(f'Digíte o sexo da {cont}º pessoa: ').upper().strip()
    idade = int(input(f'Digíte a idade da {cont}º pessoa: '))
    cont += 1
    lista.append((nome, sexo, idade))
    questao = input('Deseja continuar? [S/N] ').upper()
    if questao == 'N':
        break
for pessoa in lista:
    nome, sexo, idade = pessoa
    print(f'{nome}, {sexo}, {idade}')
    if idade > 18:
        soma_idade += 1
    if sexo == 'M':
        soma_homem += 1
    if sexo == 'F' and idade < 20:
        soma_mulher += 1

print(f'Nesta lista tem {soma_idade} pessoas com mais de 18 anos\nNesta lista tem {soma_homem} homens cadastrados\nNesta lista tem {soma_mulher} mulheres com menos de 20 anos')
