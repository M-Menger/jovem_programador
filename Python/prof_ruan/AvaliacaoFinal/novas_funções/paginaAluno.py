import os
import sys

aluno = {
        "nome": ['Matheeus','Marcos','David','Felipe'], 
        "turma": [1, 2, 3, 4],
        "notas": [[9.5, 8.2, 7.1],[8.4, 9.1, 7.5],[7.4, 8.1, 9.5],[9.4, 6.1, 3.5]], 
        "faltas": [5,4,2,0]
}

def menu():
    while True:
        opt = int(input('''
                        1.Edita nome,
                        2.Edita Turma,
                        3.Adiciona Nota,
                        4.Adiciona Falta,
                        5.Mostra Média,
                        6.Mostra Notas,
                        7.Mostra faltas,
                        0.Voltar\n
                        '''))

        print()
        while True:
            match opt:
                case 1:
                    editaNome()
                    break
                case 2:
                    os.system('cls')
                    editaTurma()
                    break
                case 3:
                    os.system('cls')
                    adicionaNota()
                    break
                case 4:
                    os.system('cls')
                    adicionaFalta()
                    break
                case 5:
                    os.system('cls')
                    mostraMedia()
                    break
                case 6:
                    os.system('cls')
                    adicionaNota()
                    break
                case 7:
                    os.system('cls')
                    mostraNotas()
                    break
                case 0:
                    os.system('cls')
                    print("Fim da aplicação")
                    sys.exit()
                case _:
                    os.system('cls')
                    print("Opção Inválida! Escolha novamente.")
                    break


def editaNome():

    if len(aluno) > 0:
        for k,v in enumerate(aluno):
            print(f'{k} | {aluno['nome'][k]}')
    else:
        print('Nenhum aluno cadastrado.')

    opt = int(input('Qual o indice do nome de aluno que deseja alterar? '))
    novoEdit = str(input('Insira o novo nome: '))

    nomeAntigo = aluno['nome'][opt]

    aluno['nome'][opt] = novoEdit

    print(f'\nO aluno {nomeAntigo} foi alterado para {aluno['nome'][opt]}.\n')
    
    menu()


def editaTurma():

    for i in range(len(aluno)):
        print(f'{i} | {aluno['nome'][i]}')

    opt = int(input('Informe o indice do aluno que você deseaja trocar de turma: '))

    if opt <= len(aluno):
        novaTurma = int(input('Para qual turma irá transferir? '))

        aluno['turma'][opt] = novaTurma 

        print(f'\nO aluno {aluno['nome'][opt]} foi trocado para a turma {aluno['turma'][opt]}.')

    else:
        print('Indice invalido.\n')
        editaTurma()

    menu()  


def adicionaNota():

    for i in range(len(aluno)):
        print(f'{i} | {aluno['nome'][i]}')

    opt = int(input('Qual aluno deseja adicionar nota? Informe o indice: '))

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
        adicionaNota()

    menu()


def adicionaFalta():

    for i in range(4):
        print(aluno['nome'][i])

    opt = int(input('Qual o nome do aluno você deseja adicionar as notas? '))
    novoEdit = str(input('Insira o número de faltas: '))


def mostraMedia():

    for i in range(4):
        print(aluno['nome'][i])



def mostraNotas():

    for i in range(4):
            print(aluno['nome'][i])


def mostraFaltas():
    for i in range(4):
        print(aluno['nome'][i])


menu()