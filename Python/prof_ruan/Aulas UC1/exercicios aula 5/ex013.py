num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

if(num1 > num2):
    print('O primeiro número foi maior! Número {}'.format(num1))
elif(num2 > num1):
    print('O Segundo número foi maior! Número {}.'.format(num2))
else:
    print('Os números são iguais! Número {}'.format(num1))