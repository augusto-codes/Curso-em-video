'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
#Biblioteca
from random import choice
import time

#Base de cor
cor_vermelha = '\033[31m'
cor_vermelha_negrito = '\033[1;31m'
cor_verde = '\033[32m'
cor_verde_negrito = '\033[1;32m'
cor_padrao = '\033[m'
negrito = '\033[1;36m'

#Chave de jogo
print('-=-' * 20)
print('Vamos brincar de adivinhação!!!')
print('-=-' * 20)

#Recebendo primeira informação do usuario
num = int(input('Digíte um número de 0 a 10: '))

#Realizando primeiros tratamento para funcionamento do jogo
tentativa = 1
lista = list(range(11))
escolha = choice(lista)
print(escolha)
lista_bool = ['N', 'S']
resposta = 'N'
pergunta = 5

#Realizando o primeiro IF para validar se já ganhamos de primeira
if num == escolha:
    print(f'{cor_verde_negrito}Parabéns meu jogador!!! Você acertou de primeira, isso foi épico{cor_padrao}')
else:
    #Caso não for de primeira vem esse while para fazer até acertar
    while num != escolha:
        tentativa += 1
        if tentativa == pergunta:
            resposta = input('Você Deseja ajuda? (S/N)\nDigíte sua resposta: ').upper()
        if resposta == 'N':
            if num in lista:
                print(f'{cor_vermelha}Você errou!! Tente novamente{cor_padrao}')
                num = int(input('Digíte um número de 0 a 10: '))
                print('Processando...\n')
                time.sleep(0.5)
            else:
                print(f'{negrito}Não seja burro!!! Os números são de 0 a 10{cor_padrao}')
                num = int(input('Digíte um número de 0 a 10: '))
                print('Processando...\n')
                time.sleep(0.5)
        elif resposta == 'S':
            if num in lista:
                    if num < escolha:
                        print(f'{cor_vermelha}Você errou!! Tente novamente, meu número é maior que {num}{cor_padrao}')
                        num = int(input('Digíte um número de 0 a 10: '))
                        print('Processando...\n')
                        time.sleep(0.5)   
                    elif num > escolha:
                        print(f'{cor_vermelha}Você errou!! Tente novamente, meu número é menor que {num}{cor_padrao}')
                        num = int(input('Digíte um número de 0 a 10: '))
                        print('Processando...\n')
                        time.sleep(0.5)
                    else:
                        print(f'{cor_vermelha_negrito}Não seja burro!!! Os números são de 0 a 10{cor_padrao}')
                        num = int(input('Digíte um número de 0 a 10: '))
                        print('Processando...\n')
                        time.sleep(0.5)
        else:
            print(f'{negrito}Cara você conseguiu errar o basico, que é digítar S ou N{cor_padrao}')
            resposta = input('Por favor, escolha novamente S para sim ou N para não: ')
if tentativa <= 5 and resposta == 'N':
    print(f'{cor_verde}Parabéns você acertou meu número em apenas {tentativa} tentativas{cor_padrao}')
elif tentativa > 5 and resposta == 'N':
    print(f'{cor_verde}Parabéns, depois de {tentativa} você conseguiu acertar meu número sem pedir ajuda{cor_padrao}')
elif tentativa >= 4 and resposta == 'S':
    print(f'{negrito}Gostaria de comemorar, porém tu só acertou depois de {tentativa} e ainda pediu ajuda...{cor_padrao}')