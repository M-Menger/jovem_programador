from math import ceil,floor

def calcula_latas(area):
    if area <= lata:
        msg = '1x Lata, totalizando 80.00R$'
    elif area > lata:
        latas = ceil(area/lata)
        msg = f'{latas}x latas, totalizando {latas*80:.2f}R$'

    return msg

def calcula_galoes(area):
    if area < galao:
        msg = f'1x Galao, totalizando 25.00R$'
    elif area > galao:
        galoes = area/galao
        galoes = ceil(galoes)
        msg = f'{galoes}x Galoes, totalizando {galoes*25:.2f}R$'
        
    return msg

def calcula_tintas(area):
    latoes = floor(area/lata)
    res = area%lata
    galoes = ceil(res/galao)

    msg = f'''\nTemos também a opcao de usar 
    {latoes}x lata(s) 
    {galoes}x Galao(oes)
      totalizando: {(latoes*80)+(galoes*25):.2f}R$\n'''

    return msg


area = float(input('Qual o tamanho da area a ser pintada: '))
lata = 108.0
galao = 21.6

areaTotal = area + (0.10*area)

print('\nBem vindo ao JPTintas:\n')
print(f'Para pintar os {area:.2f}m² temos as seguintes Opções:')
print(calcula_latas(areaTotal))
print(calcula_galoes(areaTotal))
print(calcula_tintas(areaTotal))
print('\nObs.: Consideramos 10% a mais da area total.\n')
