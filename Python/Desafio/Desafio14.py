#Conversor de temperatura
temperatura_c = input('Informe a temperatura em ºC: ').replace(',','.')
temperatura_c = float(temperatura_c)
temperatura_f = ((temperatura_c/5)*9)+32
print(f"A temperatura de {temperatura_c}ºC corresponde a {temperatura_f}ºF")