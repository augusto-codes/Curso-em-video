'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import choice

#Criando a lista da maquina
lista = list(range(1,11))
vitoria = 0


while True:
    maquina = choice(lista)
    escolha = input('Impar ou par? ').upper()
    n = int(input('Digíte um número de 0 a 10: '))
    print(f'A soma deu {n + maquina}')
    resultado = (n + maquina) % 2
    if resultado == 0:
        a = 'PAR'
    else:
        a = 'IMPAR'
    if escolha == a:
        vitoria += 1
        print('Você ganhou!!')
    else:
        print('Você perdeu...')
        break
print(f'Nesse jogo você ganhou {vitoria} vezes')
if vitoria == 0:
    print('Cara você não teve sorte...')
elif vitoria > 5:
    print(f'Parabéns campeão, você fez {vitoria} vitorias seguidas!!!')