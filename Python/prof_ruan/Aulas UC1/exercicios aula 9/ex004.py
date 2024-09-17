tamturma = int(input('Qual o tamanho da turma: '))

nomeAluno = []
notaAluno = []

if tamturma <= 30:

    for i in range(tamturma):
        aluno = str(input(f'\nDigite o nome do {i+1}° aluno: '))
        nomeAluno.append(aluno)
        nota = float(input(f'\nDigite a nota do {i+1}° aluno: '))
        notaAluno.append(nota)

    for i in range(tamturma):
        if notaAluno[i] > 7:
            print(nomeAluno[i], notaAluno[i])
else:
    print('Numero invalido!')
