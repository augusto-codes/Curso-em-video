'''O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''
import random
aluno1 = input('Digíte o nome do 1º aluno: ')
aluno2 = input('Digíte o nome do 2º aluno: ')
aluno3 = input('Digíte o nome do 3º aluno: ')
aluno4 = input('Digíte o nome do 4º aluno: ')

lista_alunos = [aluno1 , aluno2 , aluno3 , aluno4]
random.shuffle(lista_alunos)
print(f'A ordem de apresentação será {lista_alunos}')
#Opção2: print(f'A ordem de apresentação será {random.sample(lista_alunos , len(lista_alunos))}')
