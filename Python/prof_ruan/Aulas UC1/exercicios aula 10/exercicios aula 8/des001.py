from random import randint

numero = randint(1,5)

chute=int(input('Entre com um valor entre 1 e 5: '))

if chute < 1 or chute > 5:
    print('Valor invalido')
    
elif(chute == numero):
    print('Parabéns você acertou!')
else:
    print(f'Não foi dessa vez! Sorteado {numero}')
