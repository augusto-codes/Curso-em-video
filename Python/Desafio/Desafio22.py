'''Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.'''

'''Opção 1:
nome_completo = input('Digite seu nome completo: ')
nome_up = nome_completo.upper()
print(f'Em maiusiculo fica: {nome_up}')
nome_lo = nome_completo.lower()
print(f'Em minusculo fica: {nome_lo}')
nome_space = nome_completo.replace(' ','')
print(f'Seu nome tem {len(nome_space)} letras')
nome_separado = nome_completo.split()
print(f'Seu primeiro nome tem {len(nome_separado[0])} letras')'''

'''Opção 2
nome = str(input('Digíte seu nome completo: ')).strip()
print (f"""O seu nome em maiúsculo fica: {nome.upper()}
O seu nome em minúsculo fica: {nome.lower()}
Seu nome tem {len(nome.replace(' ',''))} letras
Seu primeiro nome tem {len(nome.split()[0])}""")'''

#Opção 3
nome = input('Digíte seu nome completo: ').strip()
print(f"""Analisando seu nome...
      Seu nome em letras maiúscula fica: {nome.upper()}
Seu nome em letras minúscula fica: {nome.lower()}
Seu nome tem {len(nome)-nome.count(' ')} letras
Seu primeiro nome tem {nome.find(' ')} letras""")