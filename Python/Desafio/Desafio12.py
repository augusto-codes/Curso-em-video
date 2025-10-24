print('Descruba o valor com desconto')
valor = input('Digite o valor do produto: ').replace(',','.')
valor = float(valor)
print(f'O produto com desconto é de R${valor-(valor*0.05)}'.replace('.',','))
