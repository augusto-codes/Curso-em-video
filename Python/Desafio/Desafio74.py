"""Maior e Menor Valores em Tupla: Gerar 5 números aleatórios e guardar em uma tupla. Mostrar os
números gerados, além de indicar o menor e o maior valor presente."""
from random import choice

lista = [0,1,2,3,4,5,6,7,8,9,10]
num1 = choice(lista)
num2 = choice(lista)
num3 = choice(lista)
num4 = choice(lista)
num5 = choice(lista)
tupla = (num1, num2, num3, num4, num5)

print(f"os números sorteados foram {tupla}")
menor_num = 10
maior_num = 0

for num in tupla:
    if num > maior_num:
        maior_num = num

for num in tupla:
    if num < menor_num:
        menor_num = num

print(f"O maior número é: {maior_num}")
print(f"O menor número é: {menor_num}")