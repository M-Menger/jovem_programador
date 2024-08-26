def equacao_seg_grau(a,b,c):
  delta = (b**2) - (4*a*c)
  x1 = (((-1)*b) + (delta**0.5))/(2*a)
  x2 = (((-1)*b) - (delta**0.5))/(2*a)
  if delta < 0:
    print()
    print("Delta negativo, não temos raízes reais!")

  elif delta == 0:
    print()
    print(f'Nossa equação do 2º Grau: {a}.x²{b}.x{c}= 0')
    print(f'Como Delta = 0, temos um único valor de raiz (X1 = x2): {x1:.2f}')

  else:
    print()
    print(f'Nossa equação do 2º Grau: {a}.x²{b}.x{c}= 0')
    print(f'Como Delta > 0, temos dois valores distintos de raízes: {x1:.2f} e {x2:.2f}')


a = float(input("Digite o valor de a: "))

if a == 0:
    print()
    print('Essa não é uma equação do segundo grau!')
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    equacao_seg_grau(a,b,c)
