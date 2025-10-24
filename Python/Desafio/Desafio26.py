'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''

frase = input('Digíte uma frase qualquer: ').strip()
print('Vamos ver quantas letras [a] possi em sua frase')

if frase.lower().count('a') > 0:
    print(f'Em sua frase aparece a letra [a] {frase.lower().count('a')} vezes')
    print(f'Em sua frase a primeira letra [a] aparece na posição {frase.lower().index('a')+1}')
    print(f'Em sua frase a ultima letra [a] aparece na posição {frase.lower().rindex('a')+1}')
else:
    print('Em sua frase não possui nenhuma letra [a]')