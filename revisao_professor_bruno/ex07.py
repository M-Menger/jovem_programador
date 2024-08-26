n = int(input('\nDigite o termo a ser calculado: '))

lista = [1,1]

for i in range((n-2)):
    lista.append(lista[i]+lista[(i+1)]) 

print(f'\nA série até o termo desejado fica assim: \n {lista}')
