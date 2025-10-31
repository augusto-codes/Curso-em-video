'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''
print('Vamos verificar seus dados para aprovação do emprestimo')
negado_cor = '\033[30;41m'
confirmado_cor = '\033[30;42m'
normal_cor = '\033[m'
valor_casa = float(input('Digíte o valor do imovel: '.replace(',','.')))
salario = float(input('Digíte o valor do seu salário: '.replace(',','.')))
anos_pagar = int(input('Digíte em quantos anos você deseja pagar: '))

valor_mensal = valor_casa / (anos_pagar * 12)

if valor_mensal > (salario * 0.3):
    print(f'{negado_cor}Emprestimo NEGADO!!! {normal_cor}')
else:
    print(f'{confirmado_cor}Emprestimo confirmado, PARABÉNS!!!{normal_cor}')