from tamagoshi import Tamagoshi
from menu import Menu

pet = {}

def criar_pet():
    nome = str(input('Vamos criar o nosso pet! Digite o nome: '))
    idade = int(input('Digite a idade do Pet: '))

    pet = {'Nome': nome,
            'Idade': idade}

    pet = Tamagoshi(pet['Nome'],pet['Idade'])

    print('Pet criado!')
    opt = Menu(pet)
    opt.opcoes_menu()

print('Bem vindo ao Tamagoshi!')

if len(pet) == 0:
    print('Vamos criar o seu primeiro Pet!')
    criar_pet()
else:
    opt = Menu(pet)
    opt.opcoes_menu()


