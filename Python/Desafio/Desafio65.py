'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

#Cabeçario
print(f'{'=' * 30}\nDescobrindo valores\n{'=' * 30}')
#Valores iniciais
cont = 0
soma = 0
pergunta = 'S'
maior = 0
menor = 10000000000000
#Criação do loop
while pergunta != 'N':
    n = int(input('Digíte o número do termo: '))
    soma += n
    cont += 1
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    pergunta = input('Quer continuar? (S/N)').upper()
#Finalizando o programa
print(f'Média dos valores digítados: {soma / cont}\nMaior valor lido: {maior}\nMenor valor lido: {menor}')