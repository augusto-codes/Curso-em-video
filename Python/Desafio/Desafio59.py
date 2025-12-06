'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

num1 = int(input('Digíte o primeiro número: '))
num2 = int(input('Digíte o segundo número: '))

escolha = '0'

while escolha != '5':
    escolha = input('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\n >>>>> Digíte sua opção: ')
    if escolha == '1':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif escolha == '2':
        print(f'{num1} * {num2} = {num1 * num2} ')
    elif escolha == '3':
        print(f'Primeiro número: {num1}\nSegundo número: {num2}')
        if num1 > num2:
            print(f'O número {num1} é maior que o número {num2}')
        elif num1 < num2:
            print(f'O número {num1} é menor que o número {num2}')
        else:
            print(f'Ambos números tem o mesmo valor')
    elif escolha == '4':
        num1 = int(input('Digíte o primeiro número: '))
        num2 = int(input('Digíte o segundo número: '))
    elif escolha == '5':
        break
    else:
        print('A opção selecionada não está presente na lista, por gentileza escolher uma opção valida')
        escolha = input('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\n >>>>> Digíte sua opção: ')
print('Obrigado por usar o programa!!')