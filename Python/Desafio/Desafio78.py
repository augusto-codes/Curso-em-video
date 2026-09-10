"""Maior e Menor Valores na Lista: Ler 5 valores numéricos, guardá-los em uma lista e mostrar o maior
e o menor valor digitados e suas respectivas posições na lista."""

lista = []
i = 0
for v in range(0, 5):
    lista.append(int(input(f'Digíte algum valor para a posição {i}: ')))
    i += 1

print(f'O maior valor digítado foi o {max(lista)} nas posições ', end='')
for pos, valor in enumerate(lista):
    if max(lista) == valor:
        print(f'{pos}...', end=' ')

print(f'\nO menor valor digítado foi o {min(lista)} nas posições ', end='')
for pos, valor in enumerate(lista):
    if min(lista) == valor:
        print(f'{pos}...', end=' ')



#Pratico porém o do professor estava mais completo
#print(f'O maior número: {max(lista)} e ele está na posição {lista.index(max(lista))}')
#print(f'O menor número: {min(lista)} e ele está na posição {lista.index(min(lista))}')