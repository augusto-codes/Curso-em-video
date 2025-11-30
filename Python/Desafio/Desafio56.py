'''Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

lista_pessoas = {}
soma_idade = 0
soma_mulher = 0
homem_velho = ''
idade_homem_velho = 0

for i in range(4):
    nome = str(input(f'Digíte o nome da {i + 1}ª pessoa: '))
    idade = int(input(f'Digíte a idade da {i + 1}ª pessoa: '))
    sexo = str(input(f'Digíte M para Mulher ou H para Homem, para definir o sexo da {i + 1}ª pessoa: ').upper())
    lista_pessoas[nome] = (idade, sexo)

for nome_i, (idade_i, sexo_i) in lista_pessoas.items():
    soma_idade += idade_i

    if sexo_i == 'M' and idade_i < 20:            
        soma_mulher = soma_mulher + 1
    elif sexo_i == 'H' and idade_i > idade_homem_velho:
        homem_velho = nome_i
        idade_homem_velho = idade_i

#Faz a média do grupo
print(f'A média de idade do grupo é de {soma_idade / 4}')

#Validação do homem mais velho
if idade_homem_velho != 0:
    print(f'O homem mais velho do grupo é o {homem_velho} e ele tem {idade_homem_velho} anos!!')
else:
    print('Nesse grupo não possui homens')

#Validação da quantidade de mulher do grupo
if soma_mulher == 0:
    print('Neste grupo não tem mulheres com menos de 20 anos')
elif soma_idade == 1:
    print(f'Neste grupo apenas uma mulher tem menos de 20 anos')
else:
    print(f'Neste grupo tem {soma_mulher} mulheres com menos de 20 anos')