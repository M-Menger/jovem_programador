notas = []
rpt = ''

while True:
    rpt = input('Você deseja inserir uma nota? S/N \n')
    if rpt == 's':
        notas.append(float(input('Digite uma nota: ')))
    else:
        break

copiaNotas = notas[::]

qtd = len(copiaNotas)

for i in notas:
    if i < 7:
        copiaNotas.remove(i)

print(copiaNotas)
