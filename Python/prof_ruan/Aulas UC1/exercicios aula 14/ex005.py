def pegaDados():
    a = float(input('Digite o tamanho do primeiro lado: '))
    b = float(input('Digite o tamanho do primeiro lado: '))
    c = float(input('Digite o tamanho do primeiro lado: '))

    return a, b, c


def calculaLados(a,b,c):
    if (a+b) < c or (a+c) < b:
        res = "Não é triangulo"
    elif a == b and b == c:
        res = 'Equilatero'
    elif a == b or a == c:
        res = 'Isósceles'
    elif a != b and a != c and b != c:
        res = 'Escaleno'

    return res


area = pegaDados()
resultado = calculaLados(area[0], area[1], area[2])

print(resultado)
