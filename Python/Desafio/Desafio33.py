'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''
num1 = int(input('Digíte um número: '))
num2 = int(input('Digíte um número: '))
num3 = int(input('Digíte um número: '))

#Maior - resposta retirada do chatgpt (antes havia feito um if para vericar cada num separadamente)
if num1 > num2 and num1 > num3:
    print(f'O maior número é o {num1} ')
elif num2 > num1 and num2 > num3:
    print(f'O maior número é o {num2}')
else:
    print(f'O maior número é o {num3}')

#Menor - Resposta retirada do chatgpt (antes havia feito um if para verificar cada num separadamente)
if num1 < num2 and num1 < num3:
    print(f'O menor número é o {num1}')
elif num2 < num1 and num2 < num3:
    print(f'O menor número é o {num2}')
else:
    print(f'O menor número é o {num3}')

'''Da forma que eu havia tentado anteriormente a parecia 3 resposta ao invez de duas, tudo isso por conta
da quantidade de IF mesmo utilizando o AND por algum motivo surgia 3 resposta sendo que só duas era verdadeira'''

#Maneira que eu resolveria se não fosse pela máteria do if
'''maior = max(num1, num2, num3)
menor = min(num1, num2, num3)

print(f'O maior número é o {maior}')
print(f'O menor número é o {menor}')'''

#Mandeira do professor
'''
menor = num1
if num2 < num1 and num2 < num3
    menor = num2
else:
    num3 < num1 and num3 < num2
    menor = num3

maior = num1
if num2 > num1 and num2 > num3
    maior = num2
else:
    num3 > num1 and num3 > num2
    maior = num3

print(f'O maior número é o {maior}')
print(f'O menor número é o {menor}')
'''
