print('Vamos converter valores de metros')
n1 = int(input("Digite uma quantidade de metros para ser convertida:  "))
#print(f'A quantidade de metros digitada foi de {n1} que equivale a {n1*100}cm e que em milímetros fica {n1*1000}mm')
print(f'Sua resposta convertida:\nMilímetro: {n1*1000:_.2f} mm\nCentímetro: {n1*100:_.2f} cm\nDecímetro: {n1*10:_.2f} dm\nDecâmetro: {n1/10:_.2f} dam\nHectômetro: {n1/100:_.2f} hm\nQuilômetro: {n1/1000:_.2f} km'.replace('.',',').replace('_','.'))