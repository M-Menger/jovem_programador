nomeAluno = []
notaAluno = []
piorAluno = ''

for i in range (5):
    nomeAluno.append(input('Digite o nome do aluno: '))
    notaAluno.append(float((input('Digite a nota do aluno: '))))

for i in range (5):
    if notaAluno[i] == min(notaAluno):
        piorAluno = nomeAluno[i]

print(f'O pior aluno foi {piorAluno} com nota {min(notaAluno):.2f}.')
