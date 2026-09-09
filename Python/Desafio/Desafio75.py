"""Análise de Dados em uma Tupla: Ler 4 valores pelo teclado e guardá-los em uma tupla. Mostrar:
quantas vezes apareceu o valor 9, em que posição foi digitado o primeiro valor 3 e quais foram os
números pares."""

num1 = int(input("Digíte o primeiro valor: "))
num2 = int(input("Digíte o segundo valor: "))
num3 = int(input("Digíte o terceiro valor: "))
num4 = int(input("Digíte o quarto valor: "))
tupla_num = (num1, num2, num3, num4)

print(f'{tupla_num}')
print(f"O número 9 aparece {tupla_num.count(9)} vezes")
if 3 in tupla_num:
    print(f"O primeiro valor 3 aparece na {tupla_num.index(3)+1}ª posição ")
else:
    print('NO valor 3 não foi digítado em nenhuma posição')

for num in tupla_num:
    resto = num % 2
    if resto == 0:
        print(f'O número {num} é par!!')
