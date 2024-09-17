from random import randint

sorter = randint(10,19)

vlr = int(input('Digite um valor entre 10 e 19 '))

if vlr < 10 or vlr > 19:
    print('Valor invalido!')
elif sorter == vlr:
    print(f'O número foi {sorter} parabéns você acertou!')
else:
    print(f'Não foi dessa vez! O número sorteado foi {sorter}')
