def soma(a,b):
   print(a+b)


def subtracao(a,b):
   print(a-b)


def multiplicacao(a,b):
   print(a*b)


def divisao(a,b):
    print(a/b)


a = int(input('digite o primeiro parametro: '))
b = int(input('digite o segundo parametro: '))
opt = int(input('1.Soma 2.Subtração 3.Multiplicação 4.Divisão'))

if opt == 1:
   soma(a,b)
elif opt == 2:
   subtracao(a,b)
elif opt == 3:
   multiplicacao(a,b)
elif opt == 4:
   divisao(a,b)
else:
   ('Valor errado')