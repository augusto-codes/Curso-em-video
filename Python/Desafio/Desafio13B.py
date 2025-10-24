'''Verifique o desconto do item a vista (10% de desconto) e verifique o valor parcelado (8% de acrescimo)'''
valor = input('Digite o valor do pedido: ').replace(',','.')
valor = float(valor)
print(f'O produto custa R${valor}\navista: R${valor - (valor*0.10)}\nparcelado: R${valor*1.08}')