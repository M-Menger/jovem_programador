vlr = int(input('Digite um numero: '))
res = 0

for i in range(1,vlr):
    
    if vlr % i == 0:
        res += i
    
if res == vlr:
    print(f'{vlr} é um número perfeito!')
else:
    print(f'{vlr} não é um numero perfeito!')
