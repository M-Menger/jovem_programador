vlr = int(input('Digite um numero: '))
ant = 0
prox = 1

for i in range(0, vlr-1):
    aux = prox
    prox = ant+prox
    ant = aux

print(prox)
    