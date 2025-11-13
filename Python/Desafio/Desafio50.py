'''Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''

'''#Coletando números
num1 = int(input('Digíte o primeiro número: '))
num2 = int(input('Digíte o segundo número: '))
num3 = int(input('Digíte o terceiro número: '))
num4 = int(input('Digíte o quarto número: '))
num5 = int(input('Digíte o quinto número: '))
num6 = int(input('Digíte o sexto número: '))

#Criando uma lista, montando a soma e contagem
lista = [num1, num2, num3, num4, num5, num6]
soma = 0
contagem = 0
#Realizando o FOR
for numero in lista:
    if numero % 2 == 0:
        soma = numero + soma
        contagem += 1

print(f'A soma de apenas seus números pares são {soma}')
print(f'Você digítou {contagem} números pares')'''


#forma do professor
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digíte um número: '))
    if num % 2 == 0:
        soma = soma + num
        cont += 1
print(f'Você digítou {cont} números pares e a soma deles é {soma}')
