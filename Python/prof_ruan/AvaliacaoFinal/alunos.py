import os 

alunos = list()

def menu():
    opt = str(input('''
                    A.Cadastrar aluno 
                    B.Mostrar Alunos
                    C.Remover aluno
                    D.Pagina do aluno
                    E.Sair'''))
    os.system('cls')
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

res = menu()

print(res)
    
print(cadastrar_aluno(alunos))
print(alunos)