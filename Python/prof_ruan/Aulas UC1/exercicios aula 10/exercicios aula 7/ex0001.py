qtd = int(input('Quantos valores vamos calcular a média? '))
res = 0

for i in range(0, qtd):
    vlr = float(input(f'Digite o {i+1}° valor: '))
    res += vlr
print(f'A média da turma é {vlr/qtd:.1f}')
