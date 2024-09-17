alns = int(input('Quantos alunos a turma tem? '))
res = 0

for i in range(0, alns):
    nota = float(input(f'Digite a nota do {i+1}° aluno: '))
    res += nota
print(f'A média da turma é {res/alns:.1f}')
