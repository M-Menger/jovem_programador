#
dt1 = int(input('Digite seu ano de nascimento: '))
anoatual = 2024
idade = anoatual - dt1

if (idade >= 16):
    print('Você possui {} anos e esta apto a votar!'.format(idade))
else:
    print('Você possui somente {} anos e ainda não possui idade suficiente para votar!'.format(idade))

