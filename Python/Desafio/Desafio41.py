'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''

negrito = '\033[1m'
padrao_string = '\033[m'

import datetime

print(f'''{'-=-' * 20}
Verificação de categoria do atleta, por idade
{'-=-' * 20}''')

#Data atual do sistema
agora = datetime.datetime.now()
ano_atual = agora.year

#Recebendo dado do usuario
ano_nascimento = int(input('Digíte seu ano de nascimento: '))

#Verificando a idade do usuario
idade_usuario = ano_atual - ano_nascimento

#Verificação de categoria

#Forma que eu fiz
'''if idade_usuario > 25:
    print(f'O Atleta de {idade_usuario} anos, ira competir na categoria {negrito}MASTER{padrao_string}')
elif idade_usuario > 19 and idade_usuario <= 25:
    print(f'O atleta de {idade_usuario} anos, ira competir na categoria {negrito}SÊNIOR{padrao_string}')
elif idade_usuario > 14 and idade_usuario <= 19:
    print(f'O atleta de {idade_usuario} anos, ira competir na categoria {negrito}JUNIOR{padrao_string}')
elif idade_usuario > 9 and idade_usuario <= 14:
    print(f'O atleta de {idade_usuario} anos, ira competir na categoria {negrito}INFANTIL{padrao_string}')
else:
    print(f'O atleta de {idade_usuario} anos, ira competir na categoria {negrito}MIRIM{padrao_string}')
'''
#Maneira do professor com print criado por mim
if idade_usuario <= 9:
    print(f'O atleta de {idade_usuario} anos, ira competir na categoria {negrito}MIRIM{padrao_string}')
elif idade_usuario <= 14:
    print(f'O atleta de {idade_usuario} anos, ira competir na categoria {negrito}INFANTIL{padrao_string}')
elif idade_usuario <= 19:
    print(f'O atleta de {idade_usuario} anos, ira competir na categoria {negrito}JUNIOR{padrao_string}')
elif idade_usuario <= 25:
    print(f'O atleta de {idade_usuario} anos, ira competir na categoria {negrito}SÊNIOR{padrao_string}')
else:
    print(f'O Atleta de {idade_usuario} anos, ira competir na categoria {negrito}MASTER{padrao_string}')