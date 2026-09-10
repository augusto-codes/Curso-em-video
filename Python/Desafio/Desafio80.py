"""Lista Ordenada sem Sort: O usuário digita 5 valores numéricos e o programa deve inseri-los na
posição correta da lista sem usar o método sort(). Mostra a lista ordenada ao final."""

lista = []

for cont in range(0, 5):
    valor = int(input('Digíte o valor: '))
    lista.append(valor)

lista_ordenada = []
print(min(lista))

for cont in range(0, 5):
    menor_numero = min(lista)
    print(menor_numero)
    lista_ordenada.append(menor_numero)
    lista.remove(menor_numero)

print(lista_ordenada)