'''Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''

#Primeiros input
primeiro_termo = int(input('Digíte o primeiro termo: '))
razao = int(input('Digíte o valor da P.A: '))

#Passos para rodar o WHILE
contator = 0
intermediario = 10

while intermediario != 0:
    if contator < intermediario:
        print(primeiro_termo, end=' -> ')
        contator += 1
        primeiro_termo += razao
    else:
        print('Fim')
        print('Caso queira continuar digíte qualquer valor acima de 0, caso queira finalizar digíte 0')
        intermediario = int(input('Digíte o valor: '))
        contator = 0
print('\n Obrigado por usar nosso sistema')
