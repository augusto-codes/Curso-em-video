print('Valor do aluguel do carro')
dias_utilizados = int(input('Quantos dias alugado?'))
km_percorrido = float(input('Quantos KM foi percorrido? '))
print(f'O total a pagar é de R$ {(dias_utilizados * 60) + (km_percorrido * 0.15):_.2f}'.replace('.',',').replace('_','.'))