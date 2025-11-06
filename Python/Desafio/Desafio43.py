'''Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''

#Realizando uma apresentação no terminal
print('-=-' * 20)
print('Vamos descobrir seu índice de massa corporal')
print('-=-' * 20)

#Recebendo dados do usuário e tratando os dados
peso = float(input('Digíte o quanto você pesa: ').replace(',','.'))
altura = float(input('Digíte o quanto de altura você tem: ').replace(',','.'))
imc = peso / (altura ** 2)
#Realizando a verificação de onde se encaixa
if imc < 18.5:
    print(f'Seu IMC é de {imc}, você está abaixo do peso')
elif imc < 25:
    print(f'Seu IMC é de {imc}, você está no peso ideal')
elif imc < 30:
    print(f'Seu IMC é de {imc}, você está com sobrepeso')
elif imc < 40:
    print(f'Seu IMC é de {imc}, você está com obesidade')
else:
    print(f'Seu IMC é de {imc}, você está com obesidade mórbida')
