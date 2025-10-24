'''#Faça um programa que leia o comprimento do cateto 
oposto e do cateto adjacente de um triangulo retângulo,
calcule e monstre o comprimento da hipotenusa'''
from math import pow , sqrt, hypot
cateto_oposto = input('Digíte o valor do cateto oposto: ').replace(',','.')
cateto_adjacente = input('Digíte o valor do cateto adjacente: ').replace(',','.')
cateto_oposto = float(cateto_oposto)
cateto_adjacente = float(cateto_adjacente)

#Opção1: print(f'O valor da hipotenusa é de {((float(cateto_oposto) ** 2) + (float(cateto_adjacente) ** 2)) ** (1/2):.2f}')
#Opção2: print(f'O valor da hipotenusa é de { pow((pow(float(cateto_oposto), 2) + pow(float(cateto_adjacente), 2)) , (1/2)):.2f}')
#Opção3: print(f'O valor da hipotenusa é de {sqrt(pow(cateto_oposto , 2) + pow(cateto_adjacente , 2)):.2f}')
#Opção4: print(f'O valor da hipotenusa é de {hypot(cateto_oposto, cateto_adjacente):.2f}')