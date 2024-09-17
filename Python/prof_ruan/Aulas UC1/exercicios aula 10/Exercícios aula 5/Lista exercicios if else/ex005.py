opt = int(input('Você é Homem ou Mulher? 1-Homem/2-Mulher '))
alt = float(input('Digite sua altura: '))

if(opt == 1):
    print('Para um homem da sua altura o peso ideal é {:.2f} Kgs'.format((72.7*alt)-58))
else:
    print('Para uma mulher da sua altura o peso ideal é {:.2f} Kg'.format((62.1*alt)-44.7))
    