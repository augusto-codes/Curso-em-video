'''Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''
#legenda
print('=' * 30)
print('Vamos somar números, em caso de querer sair do programa digíte 0')
print('=' * 30)

#primeira interação com o usuário
n = int(input('Digíte um o número que queira somar: '))

#Valores iniciais
cont = 0
soma = 0

#Criação do Loop
while n != 0:
    soma += n
    cont += 1
    n = int(input('Digíte um o número que queira somar: '))

print(f'Números digítados: {cont}\nSoma dos números: {soma} ')