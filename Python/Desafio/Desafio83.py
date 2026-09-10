'''Validando Expressões Matemáticas: Criar um programa onde o usuário digite uma expressão
matemática qualquer usando parênteses. O sistema deve analisar se a abertura e o fechamento dos
parênteses estão corretos e na ordem certa.'''

expressao = input('Digíte sua expressão: ')
parentese_aberto = expressao.count('(')
parentese_fechado = expressao.count(')')
if parentese_aberto != parentese_fechado:
    print(f'A expressão {expressao} é inválida!!')
else:
    if expressao.index('(') < expressao.index(')'):
        print(f'A expressão {expressao} é válida!!')
    else:
        print(f'A expressão {expressao} é inválida!!')

expr = str(input('Digite a expressão: '))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')