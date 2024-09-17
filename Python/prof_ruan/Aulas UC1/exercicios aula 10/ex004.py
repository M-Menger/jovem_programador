notas = []

for i in range(5):
    notas.append(float(input(f'Digite a {i} nota: ')))

notas.sort()

print(notas)
