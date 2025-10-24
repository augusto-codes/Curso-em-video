'''Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o último nome separadamente.'''
nome = input('Digíte seu nome completo: ').strip().title()

print(f'Seu nome completo é {nome}')
nome = nome.split()
print(f'Seu primeiro nome é {nome[0]}')
#Opção 1:Minha opção
'''print(f'Seu ultimo nome é {nome[-1]}')'''
#Opção 2: Do professor
print(f'Seu ultimo nome é {nome[len(nome)-1]}')