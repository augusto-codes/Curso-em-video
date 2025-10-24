funcionario = input('Digite o nome do funcionario: ')
valor = input('Digite o valor do salario: ').replace(',','.')
valor = float(valor)
valor_reajustado = valor*1.15
print(f'O funcionario {funcionario} com o reajuste salarial de 15% receberá apartir de hoje o salario de R${valor_reajustado:_.2f}'.replace('.',',').replace('_','.'))