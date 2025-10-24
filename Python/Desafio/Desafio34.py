'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

salario = float(input('Digíte o valor atual de seu salário em R$: ').replace(',','.'))

if salario > 1250:
    salario = salario * 1.10
else:
    salario = salario * 1.15
print(f'Salário reajusto para R${salario:_.2f}'.replace('.',',').replace('_','.'))
