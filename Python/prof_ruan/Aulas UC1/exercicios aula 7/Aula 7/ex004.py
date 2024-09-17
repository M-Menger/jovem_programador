vlr = int(input('Digite um numero: '))
primo = True

for i in range(2, vlr):
    if(vlr % i == 0):
        primo = False

    i += 1

if(primo):
    print('é primo')
else:
    print('Não é primo')
    