'''Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.'''
nome = input('Digíte o seu nome completo: ').strip().title()

#opção 1:
'''print('SILVA' in nome.upper())'''

#opção 2:
if 'SILVA' in nome.upper():
    print('No seu nome possui o sobrenome Silva, você faz parte dos 15% da população brasileira que tem o mesmo sobrenome')
else:
    print('Seu nome não possui o sobrenome Silva')