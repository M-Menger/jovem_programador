meses = ['Janeiro',
         'Fevereiro',
         'Março',
         'Abril',
         'Maio',
         'Junho',
         'Julho',
         'Agosto',
         'Setembro',
         'Outubro',
         'Novembro',
         'Dezembro']

graus = []
cont = 0

for i in meses:
    graus.append(int(input(f'Qual a temperatura média do mês de {i}: ')))

temp_media = sum(graus) / len(meses)

for i in graus:
    
    if i > temp_media:
        print(f'A temperatura do mês de {meses[cont]} mais alta que a média anual, alcançando os {i}c')
    cont += 1