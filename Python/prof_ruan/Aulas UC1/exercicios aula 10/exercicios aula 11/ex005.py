notas = []

for i in range (10):
    notas.append(float(input(f'Digite a {i+1}° nota: ')))

notas.sort()

melNotas = notas[-3:]

media = sum(melNotas)

print(f'A média das melhores notas foi {media/3:.2f}')
