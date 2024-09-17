res = True

while (res == True): 
    opt = input('Deseja somar dois numeros? sim/não ')
    if opt == 'sim':
        vlr1 = int(input('Digite o primeiro numero: '))
        vlr2 = int(input('Digite o primeiro numero: '))
 
        print(f'A soma dos numeros é {vlr1 + vlr2}')
    else:
        res = False
