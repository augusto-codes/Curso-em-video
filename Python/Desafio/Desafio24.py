'''Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”'''
print('Analise o nome da cidade...')
nome_cidade = input('Qual nome da cidade: ').strip()

#opção1: Meu própio raciocinio
'''if nome_cidade[0:5].upper() == 'SANTO':
    nome_cidade = nome_cidade.title()
    print(f'A cidade {nome_cidade} começa com Santo')
else:
    nome_cidade = nome_cidade.title()
    print(f'A cidade {nome_cidade} não começa com Santo')'''

#opção2: do curso em vídeo
print(nome_cidade[:5].upper() == 'SANTO')