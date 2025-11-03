'''Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

numero = int(input('Dígite um número inteiro: '))
selecionar_base = int(input('''Em qual base deverá ser convertido? 
[1] Binário 
[2] Octal
[3] Hexadecimal '''))

if selecionar_base == 1:
    numero_convertido = bin(numero)
    print(f'O número inteiro {numero} em binário é: {numero_convertido[2:]}')
elif selecionar_base == 2:
    numero_convertido = oct(numero)
    print(f'O número inteiro {numero} em octal é: {numero_convertido[2:]}')
elif selecionar_base == 3:
    numero_convertido = hex(numero)
    print(f'O número inteiro {numero} em hexadecimal é: {numero_convertido[2:]}')
else:
    print(f'Perdão a opção {selecionar_base} não é valida')