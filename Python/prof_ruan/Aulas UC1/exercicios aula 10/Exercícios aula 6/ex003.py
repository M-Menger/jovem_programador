qtdAluno = int(input('Quantidade de alunos: '))
i=1
somaNotas = 0.00
while(i <= qtdAluno):
    notaAluno = float(input('Digite a nota do aluno: '))
    somaNotas += notaAluno
    i +=1

media = somaNotas/qtdAluno
print(f'A média da turma: {media:.1f}')
    