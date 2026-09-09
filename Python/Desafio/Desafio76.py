"""Lista de Preços com Tupla: Criar uma única tupla que contenha nomes de produtos e seus
respectivos preços de forma sequencial. Mostrar uma listagem de preços organizada em formato
tabular."""

listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'tranferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
print('-'*40)
print(f'{"Listagem de preço":^40}')
print('-'*40)

while True:
    contador = 1
    for produto in listagem[0::2]:
        preço = float(listagem[contador])
        print(f'{produto:.<30}R$ {preço:>7.2f}')
        contador+=2
    break
print('-'*40)