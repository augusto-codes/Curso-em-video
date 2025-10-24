'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''
km = float(input('Digíte a quantidade de KMs que será percorrido: '))
if km > 200:
    print(f'O custo da viagem será de R${km * 0.45:_.2f}'.replace('.',',').replace('_','.'))
else:
    print(f'O custo da viagem será de R${km * 0.50:_.2f}'.replace('.',',').replace('_','.'))