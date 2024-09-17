nome = str(input('Digite o nome do aluno: '))
nt1 = float(input('Digite a 1° nota: '))
nt2 = float(input('Digite a 2° nota: '))
nt3 = float(input('Digite a 3° nota: '))

media = (nt1+nt2+nt3)/3

if(media >= 6 and nt1 > 4 and nt2 > 4 and nt3 > 4):
    print('Parabéns {}! Você foi aprovado com média {}.'.format(nome,media))
else:
    print('Infelizemente {}, você está reprovado!'.format('nome'))