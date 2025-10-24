'''Um professor quer sortear um dos seus quatro alunos 
para apagar o quadro. Faça um programa que ajude ele, 
lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''
import random
aluno1 = input('Digíte o nome do primeiro aluno: ')
aluno2 = input('Digíte o nome do segundo aluno: ')
aluno3 = input('Diíte o nome do terceiro aluno: ')
aluno4 = input('Diíte o nome do quarto aluno: ')

print(f'O aluno escolhido foi: {random.choice([aluno1, aluno2 , aluno3 , aluno4])}')