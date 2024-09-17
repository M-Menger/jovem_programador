import os
import sys

alunos = []


def menu():
    while True:
        opt = str(input('''
                        A. Cadastrar aluno
                        B. Mostrar Alunos
                        C. Remover aluno
                        D. Pagina do aluno
                        E. Sair\n''')).upper()

        if opt == 'A':
            cadastrar_aluno()
        elif opt == 'B':
            os.system('cls')
            mostrar_alunos()
        elif opt == 'C':
            os.system('cls')
            remover_aluno()
        elif opt == 'D':
            os.system('cls')
            menuPagAluno()
        elif opt == 'E':
            os.system('cls')
            print("Fim da aplicação")
            sys.exit()
        else:
            os.system('cls')
            print("Opção Inválida! Escolha novamente.")


def cadastrar_aluno():
    nome = input('Informe o nome do aluno: ')
    turma = int(input('Informe o código da turma: '))
    notas = []
    faltas = 0
    aluno = {
        "nome": nome,
        "turma": turma,
        "notas": notas,
        "faltas": faltas
    }
    alunos.append(aluno)
    print(f'Aluno cadastrado com sucesso!')


def mostrar_alunos():
    if len(alunos) > 0:
        for i, aluno in enumerate(alunos):
            print(f'{i} | {aluno["nome"]}')
    else:
        print('Nenhum aluno cadastrado.')


def remover_aluno():
    mostrar_alunos()
    if len(alunos) > 0:
        indice = int(input('Informe o índice do aluno que deseja remover: '))
        if 0 <= indice < len(alunos):
            del alunos[indice]
            print("Aluno removido com sucesso!")

        else:
            print("Índice inválido.")


def menuPagAluno():
    while True:
        opt = int(input('''
                        1. Editar Nome
                        2. Editar Turma
                        3. Adicionar Nota
                        4. Adicionar Falta
                        5. Mostrar Média
                        6. Mostrar Notas
                        7. Mostrar Faltas
                        0. Voltar\n'''))

        if opt == 1:
            editaNome()
        elif opt == 2:
            os.system('cls')
            editaTurma()
        elif opt == 3:
            os.system('cls')
            adicionaNota()
        elif opt == 4:
            os.system('cls')
            adicionaFalta()
        elif opt == 5:
            os.system('cls')
            mostraMedia()
        elif opt == 6:
            os.system('cls')
            mostraNotas()
        elif opt == 7:
            os.system('cls')
            mostraFaltas()
        elif opt == 0:
            os.system('cls')
            return
        else:
            os.system('cls')
            print("Opção Inválida! Escolha novamente.")


def editaNome():
    mostrar_alunos()
    if len(alunos) > 0:

        opt = int(
            input('Qual o Índice do nome de aluno que deseja alterar? '))
        if 0 <= opt < len(alunos):
            novoEdit = input('Insira o novo nome: ')
            nomeAntigo = alunos[opt]['nome']
            alunos[opt]['nome'] = novoEdit
            print(f'\nO aluno {nomeAntigo} foi alterado para {
                alunos[opt]["nome"]}.\n')
        else:
            print('Índice inválido.')


def editaTurma():
    mostrar_alunos()
    if len(alunos) > 0:

        opt = int(
            input('Informe o Índice do aluno que você deseja trocar de turma: '))
        if 0 <= opt < len(alunos):
            novaTurma = int(input('Para qual turma irá transferir? '))
            alunos[opt]['turma'] = novaTurma
            print(f'\nO aluno {alunos[opt]["nome"]} foi trocado para a turma {
                alunos[opt]["turma"]}.')
        else:
            print('Índice inválido.')


def adicionaNota():
    mostrar_alunos()
    if len(alunos) > 0:
        opt = int(input('Qual aluno deseja adicionar nota? Informe o Índice: '))
        if 0 <= opt < len(alunos):
            while True:
                res = input('Você deseja adicionar uma nota? S/N ').upper()
                if res == 'S':
                    novaNota = float(input('Digite a nota: '))
                    alunos[opt]['notas'].append(novaNota)
                elif res == 'N':
                    print(f'Notas atualizadas: {
                        alunos[opt]["nome"]} - {alunos[opt]["notas"]}')
                    break
                else:
                    print('Opção Inválida!')
        else:
            print('Índice inválido.')


def adicionaFalta():
    mostrar_alunos()
    if len(alunos) > 0:
        opt = int(
            input('Qual o índice do aluno que você deseja adicionar as faltas? '))
        if 0 <= opt < len(alunos):
            faltas = int(input('Insira o número de faltas: '))
            alunos[opt]['faltas'] += faltas
            print(f'Faltas atualizadas: {
                alunos[opt]["nome"]} - {alunos[opt]["faltas"]}')
        else:
            print('Índice inválido.')


def mostraMedia():
    mostrar_alunos()
    if len(alunos) > 0:
        opt = int(input('Qual o índice do aluno você deseja exibir a média? '))
        if 0 <= opt < len(alunos) and len(alunos[opt]['notas']) > 0:
            media = sum(alunos[opt]['notas']) / len(alunos[opt]['notas'])
            print(f'A média de {alunos[opt]["nome"]} é {media:.2f}')
        else:
            print('Índice inválido ou sem notas cadastradas.')


def mostraNotas():
    mostrar_alunos()
    if len(alunos) > 0:
        opt = int(input('Qual o índice do aluno você deseja exibir as notas? '))
        if 0 <= opt < len(alunos):
            print(f'As notas de {alunos[opt]["nome"]} são {alunos[opt]["notas"]}')
        else:
            print('Índice inválido.')


def mostraFaltas():
    mostrar_alunos()
    if len(alunos) > 0:
        opt = int(input('Qual o índice do aluno você deseja exibir as faltas? '))
        if 0 <= opt < len(alunos):
            print(f'As faltas de {alunos[opt]["nome"]} são {
                alunos[opt]["faltas"]}')
        else:
            print('Índice inválido.')


menu()
