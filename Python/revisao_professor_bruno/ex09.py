from random import choice

dados = [1,2,3,4,5,6]
sorteados = []

for i in range (0,100):
    sorteados.append(choice(dados))

for i in dados:
    print(f'O número {i} foi sorteado {sorteados.count(i)} vezes!')
