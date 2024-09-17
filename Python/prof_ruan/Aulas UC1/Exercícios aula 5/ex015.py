vlr1 = int(input('Digite o primeiro valor: '))
vlr2 = int(input('Digite o segundo valor: '))
vlr3 = int(input('Digite o terceiro valor: '))

if(vlr1 > vlr2 and vlr1 > vlr3):
    print('O primeiro valor foi maior! {}'.format(vlr1))
elif(vlr2 > vlr1 and vlr2 > vlr3):
    print('O segundo valor foi maior! {}'.format(vlr2))
else:
    print('O terceiro valor foi maior! {}'.format(vlr3))