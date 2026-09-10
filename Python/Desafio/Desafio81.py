"""Extraindo Dados de uma Lista: Ler vários números e mostrar: 
a) Quantos números foram digitados, 
b) A lista ordenada de forma decrescente  
c) Se o valor 5 foi digitado ou não na lista."""

lista = []
resposta = 's'

while resposta != 'N':
    valor = int(input('Digíte o valor: '))
    lista.append(valor)
    resposta = input('Quer continuar? [S/N]').upper()

print(f'Foram digítados {len(lista)} números')
print(sorted(lista, reverse= True))
if 5 in lista:
    print(f'O valor 5 foi digítado')
else:
    print(f'O valor 5 não foi digítado')