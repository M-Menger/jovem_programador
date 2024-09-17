import os
import sys

alunos = list()


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
                    cadastrar_aluno(alunos)
                    break
                case 'B':
                    os.system('cls')
                    mostrar_alunos(alunos)
                    break
                case 'C':
                    os.system('cls')
                    remover_aluno(alunos)
                    break
                #case 'D':
                     #os.system('cls')
                #    pagina_aluno(alunos)
                #    break
                case 'E':
                    os.system('cls')
                    print("Fim da aplicação")
                    sys.exit()
                case _:
                    os.system('cls')
                    print("Opção Inválida! Escolha novamente.")
                    break
    return opt


def cadastrar_aluno(alunos):
    nome = input('Informe o nome do aluno: ')
    turma = int(input('Informe o código da turma: '))
    notas = list()
    faltas = 0
    aluno = {
        "nome": nome,
        "turma": turma,
        "notas": notas,
        "faltas": faltas
    }
    alunos.append(aluno)

    os.system('cls')


def mostrar_alunos(alunos):
    if len(alunos) > 0:
        for k, v in enumerate(alunos):
            print(f'{k} | {v['nome']}')
    else:
        print('Nenhum aluno cadastrado.')


def remover_aluno(alunos):
    if len(alunos) == 0:
        print('Nenhum aluno cadastrado.')
    else:
        mostrar_alunos(alunos)
        indice = int(input('Informe o índice do aluno que deseja remover: '))
        del alunos[indice]


res = menu()

#print(res)

# print(cadastrar_aluno(alunos))
# print(alunos)
#print(mostrar_alunos(alunos))
