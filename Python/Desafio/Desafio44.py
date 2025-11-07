'''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros'''

valor_produto = float(input('Digíte o valor do produto: ').replace(',','.'))
escolha = input('''Escolhar a forma de pagamento
      1 - à vista dinheiro/cheque (10% de desconto)
      2 - à vista no cartão (5% de desconto)
      3 - em até 2x no cartão (preço formal)
      4 - 3x ou mais no cartão (20% de juros)
Selecione a opção: ''')

if escolha == '1':
    print(f'A vista em dinheiro ou cheque o valor ficará R$ {valor_produto - (valor_produto * 0.10):_.2f}'.replace('.',',').replace('_','.'))
elif escolha == '2':
    print(f'A vista no cartão de crédito o valor ficará R$ {valor_produto - (valor_produto * 0.05):_.2f}'.replace('.',',').replace('_','.'))
elif escolha == '3':
    print(f'O preço parcelada em duas vezes no cartão o valor ficará {valor_produto:_.2f}'.replace('.',',').replace('_','.'))
elif escolha == '4':
    print(f'O preço parcelado em três vezes ou mais o valor ficará {valor_produto + (valor_produto * 0.20):_.2f}'.replace('.',',').replace('_','.'))
else:
    print('Opção não reconhecida')

