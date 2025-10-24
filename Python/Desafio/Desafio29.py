'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''

print('Descubra se você foi multado')
velocidade = int(input('Digíte a velocidade que você estava: '))
if velocidade > 80:
    print(f'Você foi multado!!! O valor da sua multa será R${float((velocidade-80)*7):.2f}'.replace('.',','))
else:
    print(f'Você não foi multado sua velocidade era de {velocidade}, porém tome cuidado!!')
