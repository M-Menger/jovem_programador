qtd = int(input('Quantas notas serão inputadas: '))
notas = []

for i in range (qtd):
    notas.append(float(input('Digite a nota: ')))

res = sum(notas)/qtd

print(f'A média foi {res:.2f}')
