from random import choice

dado1 = [1,2,3,4,5,6]
ponto = 0
while True:

    player = choice(dado1) + choice(dado1)

    if player == 7 or player == 11:
        print(f'Parabéns você tirou {player} e ganhou!')
        break
    elif player == 2 or player == 3 or player == 12:
        print(f'Craps!!! Você tirou {player} e perdeu!')
        break
    elif player == ponto:
        print(f'Parabéns!! Você tirou novamente o número {player}!! ')
        break
    else:
        ponto = player
        print(f'Você tirou {player}')
