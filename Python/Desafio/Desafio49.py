'''Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''
numero_usuario = int(input('Digíte o número que deseja saber a tabuada: '))
for i in range(0, 10):
    print(f'{numero_usuario} X {i+1} = {numero_usuario * (i + 1)}')