'''Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''

#Seleção de cores para o terminal
aprovado_cor = '\033[1;32m'
reprovado_cor = '\033[1;31m'
recuperacao_cor = '\033[1;33m'
padrao_cor = '\033[m'

#Coletando dados
print('Olá, vamos verificar se seu aluno foi aprovado ou não')
nota1 = float(input('Digíte a nota do primeiro semestre: ').replace(',','.'))
nota2 = float(input('Digíte a nota do segundo semestre: ').replace(',','.'))
media = (nota1 + nota2) / 2

#Imprimindo dados coletados
print(f'''Nota primeiro semestre: {nota1}
Nota segundo semestre: {nota2}
Nota final: {media}''')

#Realizando a comparação para saber o resultado
if media >= 7:
    print(f'Está {aprovado_cor}APROVADO!!{padrao_cor}')
elif media >= 5 and media <= 6.9:
    print(f'Está em{recuperacao_cor} RECUPERAÇÃO{padrao_cor}')
else:
    print(f'Está {reprovado_cor}REPROVADO!!{padrao_cor}')
