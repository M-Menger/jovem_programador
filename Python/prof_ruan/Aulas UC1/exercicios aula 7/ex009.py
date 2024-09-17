res = 0
for i in range(0,20):
    vlr = int(input('Digite um valor: '))
    if vlr % 2 == 0:
        res += 1
print(f'Temos {res} numeros pares')
