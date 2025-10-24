print('Vamos descobrir quantos dólar você poderia ter em sua carteira')
carteira = input("Digite o quantos você tem em sua carteira: ".replace(',','.'))
carteira = float(carteira)
print(f'O saldo de sua carteira é de R${carteira} que equivale a US${carteira/3.27:.2f}'.replace('.',','))