'''Dividindo Valores em Múltiplas Listas: Ler vários números e colocar em uma lista principal. Depois,
criar duas listas extras: uma apenas com números pares e outra com ímpares. Mostrar as três listas no
final.'''

lista = []
resposta = 'S'
impar = []
par = []

while resposta != 'N':
    valor = int(input('Digíte o valor: '))
    resposta = input('Deseja continuar? [S/N]').upper()
    lista.append(valor)
    resto = valor % 2
    if resto == 0:
        par.append(valor)
    else:
        impar.append(valor)

print('-='*30)
print(f'Lista completa: {lista}')
print(f'Lista de pares: {par}')
print(f'Lista de impares: {impar}')