lista = [0]*8
res = 0
pos = 0

for i in range(8):
    lista[i] = int(input(f'Digite o {i+1}° valor: '))
    res += lista[i]

    if lista[i] > 0:
        pos += 1
print(f'A soma dos valores é {res}, e tem um total de {pos} números positivos.')
