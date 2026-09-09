""" Contando Vogais em Tupla: Criar uma tupla com várias palavras. O programa deve analisar cada
palavra e exibir quais são as suas vogais """

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} ', end='')
    for letra in palavra:
        if letra.lower() in'aeiou':
            print(letra, end=' ')
    
