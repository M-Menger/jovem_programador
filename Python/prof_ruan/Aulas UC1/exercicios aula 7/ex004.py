vlr1 = int(input('Digite o primeiro valor: '))
vlr2 = int(input('Digite o segundo valor: '))

if (vlr1 < vlr2):
    for i in range(vlr1,vlr2+1):
        print(i)
else:
    for i in range(vlr2,vlr1+1):
        print(i)
