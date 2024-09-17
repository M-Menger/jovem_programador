rpt = True
while(rpt == True):
    a = int(input('Digite o primeiro valor: '))
    b = int(input('Digite o segundo valor: '))
    if(a > b):
        print(a)
    elif(a < b):
        print(b)
    else:
        print('Numeros iguais')
        rpt = False
