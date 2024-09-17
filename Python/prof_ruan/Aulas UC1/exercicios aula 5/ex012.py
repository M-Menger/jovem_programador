num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo número: '))

if(num2 == 0):
    print('Valor invalido, 0 não é permitido nesta operação.')
else:
    print('Valor {:.2f} dividido por {:.2f} é {:.2f}!'.format(num1,num2,num1/num2))

