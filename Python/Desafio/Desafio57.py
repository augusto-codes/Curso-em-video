'''Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

sexo = input('Qual é seu gênero? \n(Digíte M se for masculino ou digíte F para feminino)\n Digíte sua escolha: ').upper()

while sexo != 'M' and sexo != 'F':
    sexo = input('Desculpe eu não entendi!!\n(Digíte M se for masculino ou digíte F para feminino)\n Digíte sua escolha: ').upper()

if sexo == 'M':
    print('Sua escolha foi M, você é do gênero masculino')
else:
    print('Sua escolha foi F, você é do gênero feminino')
