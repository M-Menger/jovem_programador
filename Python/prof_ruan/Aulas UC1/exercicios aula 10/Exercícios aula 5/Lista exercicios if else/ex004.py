vlr1 = int(input('Digite o 1° valor: '))
vlr2 = int(input('Digite o 2° valor: '))
vlr3 = int(input('Digite o 3° valor: '))

if(vlr1 == vlr2 or vlr1 == vlr3 or vlr2 == vlr3):
    print('Os valores estão repetidos!')
elif(vlr1 < vlr2 < vlr3):
    print('Valores: {}, {}, {}.'.format(vlr1,vlr2,vlr3))
elif(vlr1 < vlr3 < vlr2):
    print('Valores: {}, {}, {}.'.format(vlr1,vlr3,vlr2))
elif(vlr2 < vlr1 < vlr3):
   print('Valores: {}, {}, {}.'.format(vlr2,vlr1,vlr3))
elif(vlr2 < vlr3 < vlr1):
   print('Valores: {}, {}, {}.'.format(vlr2,vlr3,vlr1))
elif(vlr3 < vlr1 < vlr2):
   print('Valores: {}, {}, {}.'.format(vlr3,vlr1,vlr2))
else:
    print('Valores: {}, {}, {}.'.format(vlr3,vlr2,vlr1))
    