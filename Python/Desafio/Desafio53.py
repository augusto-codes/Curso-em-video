'''Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''
cor_vermelha = '\033[31m'
cor_verde = '\033[32m'
cor_padrao = '\033[m'
negrito = '\033[1;36m'

texto = input('Digíte o texto: ').strip().upper()
palavras = texto.split()
junto = ''.join(palavras)
inverso = junto[::-1]

print(f'O inverso de {negrito}{junto}{cor_padrao} é {negrito}{inverso}{cor_padrao}')

if junto == inverso:
    print(f'{cor_verde}Temos um palíndromo{cor_padrao}')
else:
    print(f'{cor_vermelha}Não foi dessa vez... Essa frase não é um palindromo{cor_padrao}')
