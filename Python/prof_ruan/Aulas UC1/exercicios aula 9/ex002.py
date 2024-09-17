lista = [0]*8

for i in range(8):
    lista[i] = int(input(f'Digite o {i+1}° valor: '))
    
for i in range(7,-1,-1):
    print(lista[i])
