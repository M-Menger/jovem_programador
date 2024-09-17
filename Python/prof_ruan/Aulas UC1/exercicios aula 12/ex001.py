frase = str(input('Digite uma frase: '))

teste = frase[::-1]

if frase == teste:
    print('É palíndromo')
else:
    print('Não é palíndromo')
