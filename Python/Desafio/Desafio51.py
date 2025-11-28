'''Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''

print('='*20)
print('Progressão Aritmética')
print('='*20)

#Forma que eu fiz
'''a1 = int(input('Digíte o primeiro termo da P.A: '))
razao = int(input('Digíte o valor da razão de sua P.A: '))

print(a1)
for c in range(1, 10):
    a1 = a1 + razao
    print(a1)
'''

#Forma prática
primeiro_termo = int(input('Digíte o primeiro termo: '))
razao = int(input('Dígite o valor da razão: '))

#Forma de sempre pegar até 10º termo da P.A
decimo_termo = primeiro_termo + (10 - 1) * razao

for c in range(primeiro_termo, decimo_termo + razao, razao):
    print(f'{c}', end= ' -> ')
print('Acabou')