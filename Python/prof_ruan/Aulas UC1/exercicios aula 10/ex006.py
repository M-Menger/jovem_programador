nomeAluno = []
notaAluno = []
piorAluno = ''

for i in range (5):
    nomeAluno.append(input('Digite o nome do aluno: '))
    notaAluno.append(float((input('\nDigite a nota do aluno: '))))

for i in range (5):
    if notaAluno[i] == max(notaAluno):
        piorAluno = nomeAluno[i]

print(f'O melhor aluno foi {piorAluno} com nota {max(notaAluno):.2f}.')
