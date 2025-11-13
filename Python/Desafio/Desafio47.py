'''Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.'''

#Meu jeito
'''for i in range(0, 51, +1):
    if i % 2 == 0:
        print(i)
print('Acabou')'''

#Mandeira do professor
for i in range(2, 51, 2):
    print(i, end=' ') # 'end' funciona para deixar tudo na mesma linha
print('Acabou')