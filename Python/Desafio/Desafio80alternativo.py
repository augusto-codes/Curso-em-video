lista = []

for cont in range(0, 5):
    valor = int(input('Digíte o valor: '))
    lista.append(valor)

lista_ordenada = []

#ele vai pegar os número da lista que serão comparado
for valor_menor in lista:
    if not lista_ordenada:
        lista_ordenada.append(valor_menor)
    elif valor_menor <= lista_ordenada[0]:
        lista_ordenada.insert(0, valor_menor)
    elif len(lista_ordenada) < 2 or valor_menor < lista_ordenada[1]:
        lista_ordenada.insert(1, valor_menor)
    elif len(lista_ordenada) < 3 or valor_menor < lista_ordenada[1]:
        lista_ordenada.insert(2, valor_menor)
    elif len(lista_ordenada) < 4 or valor_menor < lista_ordenada[1]:
        lista_ordenada.insert(3, valor_menor)
    elif len(lista_ordenada) < 5 or valor_menor < lista_ordenada[1]:
        lista_ordenada.insert(4, valor_menor)
print(lista_ordenada)