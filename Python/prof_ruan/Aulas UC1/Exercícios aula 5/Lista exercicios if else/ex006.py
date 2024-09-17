lados = int(input('Digite o número de lados: '))
medida = float(input('Digite a medida dos lados em cm: '))

if (lados == 3):
    print('TRIÂNGULO de {:.2f} Cm'.format(lados*medida))
elif(lados == 4):
    print('QUADRADO de {:.2f} Cm'.format(lados*medida))
elif(lados == 5):
    print('PENTAGONO de {:.2f} Cm'.format(lados*medida))
else:
    print('Quantidade de lados invalida!')