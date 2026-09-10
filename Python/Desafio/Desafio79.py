"""Valores Únicos em uma Lista: O usuário pode cadastrar vários valores numéricos. Se o número já
existir na lista, ele não será adicionado. Ao final, exibir os valores cadastrados em ordem crescente."""
lista = []
resposta = 'S'
repitido = 0
while resposta != 'N':
    valor = int(input('Digíte um valor: '))
    if valor in lista:
        print('Esse número já foi, tente outro!!')
        repitido += 1
        resposta = input('Você dejesa continuar? [S/N]\n')
        resposta = resposta.upper()
    
    else:
        lista.append(valor)
        resposta = input('Você dejesa continuar? [S/N]\n')
        resposta = resposta.upper()
print(sorted(lista))
print(f'Você tentou colocar {repitido} o mesmo número na lista!!')