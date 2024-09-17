ld1 = float(input('Digite o tamanho do primeiro lado: '))
ld2 = float(input('Digite o tamanho do segundo lado: '))
ld3 = float(input('Digite o tamanho do terceiro lado: '))

if(ld1 == ld2 == ld3):
    print('Triangulo Equilátero!')
elif(ld1 == ld2 or ld1 == ld3 or ld2 == ld3):
    print('Triangulo Isóscele!')
else:
    print('Triângulo Escaleno!')