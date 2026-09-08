"""Número por Extenso: Criar uma tupla preenchida com uma contagem por extenso de zero até vinte. O

programa deve ler um número pelo teclado e mostrá-lo por extenso."""
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    input_num = input('Digíte um número de 0 a 20: \n')
    input_num = int(input_num)
    if input_num >= 0 and input_num<= 20:
        break
    else:
        print(f"Tente novamente.")

print(f"Você diigítou o número {numeros[input_num]}")