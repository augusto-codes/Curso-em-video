'''Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''
#Criando um título
print(f'{'=' * 30}\nSUPER SOMADOR\n{'=' * 30}')
#Criando valores de parametros
s = 0
cont = 0
#Criando um loop infinito
while True:
    n = int(input('Você deve digitar o número que queira somar, caso o número seja 0 o programa irar finalizar\nDigíte o número: '))
    #Coloquei 0 por que para mim fez mais sentido ao programa, já que ele não é somavel
    if n == 0:
        break
    s += n
    cont += 1
print(f'Você digítou {cont} números e a soma de todos colocado deu {s}')