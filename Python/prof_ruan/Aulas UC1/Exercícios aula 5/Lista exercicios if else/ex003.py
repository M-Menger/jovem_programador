qtd = int(input('Quantas maçãs você irá levar: '))

if(qtd <= 12):
    print('O valor total das suas compras ficou em: {}R$'.format(qtd*0.30))
else:
    print('O valor total das suas compras ficou em: {}R$'.format(qtd*0.25))