import os
import sys

alunos = {
        "nome": ['Matheeus','Marcos','David','Felipe'], 
        "turma": [1, 2, 3, 4],
        "notas": [[9.5, 8.2, 7.1],[8.4, 9.1, 7.5],[7.4, 8.1, 9.5],[9.4, 6.1, 3.5]], 
        "faltas": [5,4,2,0]
}


def menu():
    while True:
        opt = str(input('''
                        A. Cadastrar aluno 
                        B. Mostrar Alunos
                        C. Remover aluno
                        D. Pagina do aluno
                        E. Sair\n'''))

        print()
        while True:
            match opt.upper():
                case 'A':
                    cadastrar_aluno()
                    break
                case 'B':
                    os.system('cls')
                    mostrar_alunos()
                    break
                case 'C':
                    os.system('cls')
                    remover_aluno()
                    break
                case 'D':
                    os.system('cls')
                    menuPagAluno()
                    break
                case 'E':
                    os.system('cls')
                    print("Fim da aplicação")
                    sys.exit()
                case _:
                    os.system('cls')
                    print("Opção Inválida! Escolha novamente.")
                    break
        return opt


def cadastrar_aluno():
    nome = input('Informe o nome do aluno: ')
    turma = int(input('Informe o código da turma: '))
    notas = list()
    faltas = 0
    alunos['nome'].append(nome)
    alunos['turma'].append(turma)
    alunos['notas'].append(notas)
    alunos['faltas'].append(faltas)

    print(f'Aluno cadastrado com sucesso!')
    menu()
    os.system('cls')


def mostrar_alunos():
    if len(alunos) > 0:
        for i in range(len(alunos)):
            print(f'{i} | {alunos['nome'][i]}')
    else:
        print('Nenhum aluno cadastrado.')
    menu()
        

def remover_aluno():
    mostrar_alunos()
    indice = int(input('Informe o índice do aluno que deseja remover: '))
    del alunos['nome'][indice]
    del alunos['turma'][indice]
    del alunos['notas'][indice]
    del alunos['faltas'][indice]   
    menu()


def menuPagAluno():
    while True:
        opt = int(input('''
                        1.Editar Nome,
                        2.Editar Turma,
                        3.Adicionar Nota,
                        4.Adicionar Falta,
                        5.Mostrar Média,
                        6.Mostrar Notas,
                        7.Mostrar Faltas,
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
                    mostraNotas()
                    break
                case 7:
                    os.system('cls')
                    mostraFaltas()
                    break
                case 0:
                    os.system('cls')
                    menu()
                case _:
                    os.system('cls')
                    print("Opção Inválida! Escolha novamente.")
                    break


def editaNome():

    if len(alunos) > 0:
        for k,v in enumerate(alunos):
            print(f'{k} | {alunos['nome'][k]}')
    else:
        print('Nenhum aluno cadastrado.')

    opt = int(input('Qual o Índice do nome de aluno que deseja alterar? '))
    if opt<=len(alunos):
        novoEdit = str(input('Insira o novo nome: '))
        nomeAntigo = alunos['nome'][opt]
        alunos['nome'][opt] = novoEdit
        print(f'\nO aluno {nomeAntigo} foi alterado para {alunos['nome'][opt]}.\n')
    else: 
        print('Índice inválido.\n')
        editaNome()
    menuPagAluno()


def editaTurma():

    for i in range(len(alunos)):
        print(f'{i} | {alunos['nome'][i]}')
    opt = int(input('Informe o Índice do aluno que você deseaja trocar de turma: '))

    if opt <= len(alunos):
        novaTurma = int(input('Para qual turma irá transferir? '))
        alunos['turma'][opt] = novaTurma 
        print(f'\nO aluno {alunos['nome'][opt]} foi trocado para a turma {alunos['turma'][opt]}.')
    else:
        print('Índice inválido.\n')
        editaTurma()
    menuPagAluno()  


def adicionaNota():

    for i in range(len(alunos)):
        print(f'{i} | {alunos['nome'][i]}')
    opt = int(input('Qual aluno deseja adicionar nota? Informe o Índice: '))

    if opt <= len(alunos):
        while True:
            res = input('Você deseja adicionar uma nota? S/N ')
            if res.upper() == 'S':
                novaNota = float(input('Digite a nota: '))
                alunos['notas'][opt].append(novaNota)
            elif res.upper() == 'N':
                print(f'Notas atualizadas, {alunos['nome'][opt]} {alunos['notas'][opt]}')
                break
            else :
                print('Opção Inválida!')
                adicionaNota()               
    else:
        print('Índice inválido\n')
        adicionaNota()
    menuPagAluno()


def adicionaFalta():

    for i in range(len(alunos['nome'])):
        print(f'{i} | {alunos['nome'][i]}')
    opt = int(input('Qual o índice do aluno você deseja adicionar as faltas? '))

    if opt <= len(alunos['nome']):
        faltas = int(input('Insira o número de faltas: '))
        alunos['faltas'][opt] += faltas
    else:
        print('Opção inválida')
        adicionaFalta()


def mostraMedia():

    for i in range(len(alunos)):
        print(f'{i} | {alunos['nome'][i]}')
    opt = int(input('Qual o índice do aluno você deseja exibir a média? '))

    if opt <= len(alunos) : 
        media = (sum(alunos['notas'][opt]))/len(alunos['notas'][opt])
        print (f'A média de {alunos['nome'][opt]} é {media:.2f}')
        res = str(input('Deseja verificar a média de outro aluno? S/N \n'))
        if res.upper() == 'S' : 
            mostraMedia()
        elif res.upper() == 'N':
            menuPagAluno()
        else:
            print('Valor invalido!')
            menuPagAluno()
            
    else:
        print('Índice inválido\n')
        mostraMedia()


def mostraNotas():

    for i in range(len(alunos)):
        print(f'{i} | {alunos['nome'][i]}')
    opt = int(input('Qual o índice do aluno você deseja exibir as notas? '))
    
    if opt <= len(alunos) :
        if len(alunos['notas'][opt]) > 0: 
            print (f'As notas de {alunos['nome'][opt]} são {alunos['notas'][opt]}')

            res = str(input('Deseja verificar as faltas de outro aluno? S/N \n'))
            if res.upper() == 'S' : 
                mostraNotas()
            elif res.upper() == 'N':
                menuPagAluno()
            else:
                print('Valor invalido!')
                menuPagAluno()
        else :
            print ('Nenhuma nota cadastrada')
    else:
        print('Índice inválido\n')
        mostraNotas()


def mostraFaltas():
    
    for i in range(len(alunos)):
        print(f'{i} | {alunos['nome'][i]}')
    opt = int(input('Qual o índice do aluno você deseja exibir as faltas? '))
    
    if opt <= len(alunos) :
        print (f'As faltas {alunos['nome'][opt]} são {alunos['faltas'][opt]}')

        res = str(input('Deseja verificar as faltas de outro aluno? S/N \n'))
        if res.upper() == 'S' : 
            mostraFaltas()
        elif res.upper() == 'N':
            menuPagAluno()
        else:
            print('Valor invalido!')
            menuPagAluno()
    else:
        print('Índice inválido\n')
        mostraFaltas()


menu()
