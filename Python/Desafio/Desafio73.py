"""Tupla com Times de Futebol: Armazenar os 20 primeiros colocados do Campeonato Brasileiro.
Mostrar:
Os 5 primeiros
Os últimos 4 colocados
Os times em ordem alfabética
A posição de um time
"""
times = ('Flamengo', 'Palmeiras', 'Athletico_PR', 'Fluminense', 'Bahia', 'Cruzeiro', 'Coritiba', 'Atlético Mineiro', 'Bragantino', 'São Paulo', 'Vitória', 'Corinthians', 'Santos', 'Botafogo', 'Grêmio', 'Mirassol', 'Vasco', 'Internacional', 'Remo', 'Chapecoense')
print(f'Lista de time brasileirão: {times}')
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(f'Os 5 primeiros times do brasileirão 2026 são: {times[0:6]}')
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(f'Os últimos 4 colocados desse ano são: {times[16:]}')
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(f'Times em ordem alfabética: {sorted(times)}')
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
while True:
    time = input('Digíte o nome de seu time : ')
    if time in times:
        print(f'O {time}, está em {times.index(time) + 1}º no Campeonato Brasileiro')
        break
    else:
        print(f'Verifique se o {time} está escrito certo, ou se ele está na tabela do Brasileirão 2026')