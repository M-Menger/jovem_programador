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

    opt = int(input('Qual o Índice do nome de aluno que deseja alterar? '))
    if opt<=len(aluno):
        novoEdit = str(input('Insira o novo nome: '))

        nomeAntigo = aluno['nome'][opt]

        aluno['nome'][opt] = novoEdit

        print(f'\nO aluno {nomeAntigo} foi alterado para {aluno['nome'][opt]}.\n')
    else: 
        print('Índice inválido.\n')
        editaNome()
    
    menu()


def editaTurma():

    for i in range(len(aluno)):
        print(f'{i} | {aluno['nome'][i]}')

    opt = int(input('Informe o Índice do aluno que você deseaja trocar de turma: '))

    if opt <= len(aluno):
        novaTurma = int(input('Para qual turma irá transferir? '))

        aluno['turma'][opt] = novaTurma 

        print(f'\nO aluno {aluno['nome'][opt]} foi trocado para a turma {aluno['turma'][opt]}.')

    else:
        print('Índice inválido.\n')
        editaTurma()

    menu()  


def adicionaNota():

    for i in range(len(aluno)):
        print(f'{i} | {aluno['nome'][i]}')

    opt = int(input('Qual aluno deseja adicionar nota? Informe o Índice: '))

    if opt <= len(aluno):
        while True:
            res = input('Você deseja adicionar uma nota? S/N ')
            if res.upper() == 'S':
                novaNota = float(input('Digite a nota: '))
                aluno['notas'][opt].append(novaNota)
            elif res.upper() == 'N':
                print(f'Notas atualizadas, {aluno['nome'][opt]} {aluno['notas'][opt]}')
                break
            else :
                print('Opção Inválida!')
                adicionaNota()
                
    else:
        print('Índice inválido\n')
        adicionaNota()

    menu()


def adicionaFalta():

    for i in range(len(aluno['nome'])):
        print(f'{i} | {aluno['nome'][i]}')

    opt = int(input('Qual o índice do aluno você deseja adicionar as faltas? '))
    if opt <= len(aluno['nome']):
        faltas = int(input('Insira o número de faltas: '))
        aluno['faltas'][opt] += faltas
    else:
        print('Opção inválida')
        adicionaFalta()


def mostraMedia():

    for i in range(len(aluno)):
        print(f'{i} | {aluno['nome'][i]}')
    opt = int(input('Qual o índice do aluno você deseja exibir a média? '))
    if opt <= len(aluno) : 
        media = (sum(aluno['notas'][opt]))/len(aluno['notas'][opt])
        print (f'A média de {aluno['nome'][opt]} é {media:.2f}')

        res = str(input('Deseja verificar a média de outro aluno? S/N \n'))
        if res.upper() == 'S' : 
            mostraMedia()
        elif res.upper() == 'N':
            menu()
        else:
            print('Valor invalido!')
            menu()
            
    else:
        print('Índice inválido\n')
        mostraMedia()




def mostraNotas():

    for i in range(len(aluno)):
        print(f'{i} | {aluno['nome'][i]}')
    opt = int(input('Qual o índice do aluno você deseja exibir as notas? '))
    
    if opt <= len(aluno) :
        if len(aluno['notas'][opt]) > 0: 
            print (f'As notas de {aluno['nome'][opt]} são {aluno['notas'][opt]}')

            res = str(input('Deseja verificar as faltas de outro aluno? S/N \n'))
            if res.upper() == 'S' : 
                mostraNotas()
            elif res.upper() == 'N':
                menu()
            else:
                print('Valor invalido!')
                menu()
        else :
            print ('Nenhuma nota cadastrada')
    else:
        print('Índice inválido\n')
        mostraNotas()


def mostraFaltas():
    
    for i in range(len(aluno)):
        print(f'{i} | {aluno['nome'][i]}')
    opt = int(input('Qual o índice do aluno você deseja exibir as faltas? '))
    
    if opt <= len(aluno) :
        print (f'As faltas {aluno['nome'][opt]} são {aluno['faltas'][opt]}')

        res = str(input('Deseja verificar as faltas de outro aluno? S/N \n'))
        if res.upper() == 'S' : 
            mostraFaltas()
        elif res.upper() == 'N':
            menu()
        else:
            print('Valor invalido!')
            menu()
    else:
        print('Índice inválido\n')
        mostraFaltas()



menu()

