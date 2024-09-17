lista = [0]*5
i = 0
valida = -1

for i in range(5):
    lista[i] = input('Digite um valor: ')

aut = input('Encontre um valor: ')

for i in range(5):
    if aut == lista[i]:
        valida = i

if valida == -1:
    print(valida)
else:
    print(f'O valor esta na posição[{valida}]')