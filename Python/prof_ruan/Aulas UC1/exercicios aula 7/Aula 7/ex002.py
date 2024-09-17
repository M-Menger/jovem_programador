vlr = int(input('Digite um numero: '))
res = 1

for i in range(0,vlr):
    res += res*i
print(f'Fatorial de {vlr} é {res}')
