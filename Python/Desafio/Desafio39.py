'''Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
import datetime

#Cores do terminal
negado_cor = '\033[30;41m'
confirmado_cor = '\033[30;42m'
normal_cor = '\033[m'

#Verificação da data atual, input sobre a data de nascimento e verificação da possivel idade da pessoa
agora = datetime.datetime.now()
ano_atual = agora.year
ano_nascimento = int(input('Digíte o ano de seu nascimento: '))
idade = ano_atual - ano_nascimento

if idade > 18:
    print(f'{negado_cor}Você possui {idade} anos, seu alistamento já passou do prazo, você deveria ter se alistado em {ano_atual - (idade - 18)}.{normal_cor}')
elif idade == 18:
    print(f'{confirmado_cor}Você possui {idade}, você deve ser alistar esse ano!!!{normal_cor}')
else:
    print(f'Você possui {idade}, ainda não chegou seu tempo, você deverá se alistar em {(18 - idade) + ano_atual}.')
