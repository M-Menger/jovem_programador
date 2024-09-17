notas = []
cont = 0

for i in range(5):
    notas.append(float(input('Digite a nota: ')))

    for i in notas:
        if i < 8:
            notas.remove(i)

print(notas)
