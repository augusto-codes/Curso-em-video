'''Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais'''

num1 = int(input('Digíte um número inteiro: '))
num2 = int(input('Digíte outro número inteiro ou o mesmo: '))

if num1 > num2:
    print('O primeiro valor é MAIOR')
elif num1 < num2:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')