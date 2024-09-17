massa = float(input('Qual seu peso? '))
altura = float(input('Qual a sua altura? '))

imc = massa /(altura*2)

if(imc < 18.5):
    print('Abaixo do peso.')
elif(imc <= 25):
    print('Saudável')
elif(imc <= 30):
    print('Peso em excesso')
elif(imc <= 35):
    print('Obesidade Grau I')
elif(imc <= 40):
    print('Obesidade Grau II (severa)')
else:
    print('Obesidade Grau III (morbida)')