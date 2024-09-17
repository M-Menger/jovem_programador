massa = float(input('Qual seu Peso: '))
altura = float(input('Qual sua altura: '))
imc = massa/(altura*2)

if(imc < 18.5):
    print('IMC {:.2f} Abaixo do Peso!'.format(imc))
elif(imc < 25):
    print('IMC {:.2f} Saudável!'.format(imc))
elif(imc < 30):
    print('IMC {:.2f} Peso em excesso!'.format(imc))
elif(imc < 35):
    print('IMC {:.2f} Obesidade Grau I'.format(imc))
elif(imc < 40):
    print('IMC {:.2f} Obesidade Grau I (severa)'.format(imc))
else:
    print('IMC {:.2f} Obesidade Grau III(mórbida'.format(imc))