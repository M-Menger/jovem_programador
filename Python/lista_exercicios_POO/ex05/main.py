from macaco import Macaco

monkeys = {}

def cria_macaco():
    global monkeys
    print('Crie seus macacos!')
    nome = str(input('Crie seu Macaco, dê um nome a ele: '))
    bucho = str(input('Qual o estomago dele? '))
    
    monkeys = {'Nome':nome,'Bucho':bucho}

    menu()

def alimentar():
    ...
        
def menu():
    print('\n---Menu---\n')
    print('a) Criar Macacos')
    print('b) Menu\n')
    opt = str(input('O que você deseja fazer: \n\n'))

    match opt.lower():
        case 'a':
            cria_macaco()
        case 'b':
            ...
        case 'c':
            menu()
        case _:
            print('Opção Invalida!\n')
            return menu()

menu()