aluno = {
        "nome": ['Matheus','Marcos','David','Felipe'], 
        "turma": [1, 2, 3, 4],
        "notas": [[9.5, 8.2, 7.1],[8.4, 9.1, 7.5],[7.4, 8.1, 9.5],[9.4, 6.1, 3.5]], 
        "faltas": [5,4,2,0]
}


def adicionaFalta():

    for i in range(len(aluno)):
        print(f'{i} | {aluno['nome'][i]}')

    opt = int(input('Qual aluno deseja adicionar falta? Informe o indice: '))

    if opt <= len(aluno):
        while True:
            res = input('Você deseja adicionar uma nota? S/N ')
            if res.upper() == 'S':
                novaNota = float(input('Digite a nota: '))
                aluno['notas'][opt].append(novaNota)
            else:
                print(f'Notas atualizadas, {aluno['nome'][opt]} {aluno['notas'][opt]}')
                break
    else:
        print('Indice invalido\n')



adicionaFalta()

print(aluno['nome'])



#print(f'{k} | {v['nome']}')
