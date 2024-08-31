class Menu():
    def __init__(self, pet):
        self.pet = pet


    def alimentar_pet(self):
        print('\nO que você quer dar ao seu Pet? ')
        print('A) - Ração (Fome +10 / Humor -5)')
        print('B) - Biscoito (Fome +5 / Humor +2)')
        opt = str(input('Digite a opção Desejada: '))
        
        match opt.lower():
            case 'a':
                food = 'Ração'
            case 'b':
                food = 'Biscoito'
            case _:
                print('Opção Invalida!')
                return self.alimentar_pet()
        
        self.pet.set_alimentar(food)
        self.pet.get_fome()
        print('')
        self.opcoes_menu()

    def brincar_pet(self):
        print('\nComo você quer brincar com seu Pet? ')
        print('A) - Pega bolinha (Humor +15 / Fome -7)')
        print('B) - Cocegas (Humor +10)')
        opt = str(input('Digite a opção Desejada: '))
        
        match opt.lower():
            case 'a':
                joke = 'Pega bolinha'
            case 'b':
                joke = 'Biscoito'
            case _:
                print('Opção Invalida!')
                return self.brincar_pet()
        
        self.pet.set_brincar(joke)
        self.pet.get_humor()
        print('')
        self.opcoes_menu()
    
    def get_status(self):
        self.pet.get_humor()
        self.pet.get_fome()
        self.opcoes_menu()

    def get_name(self):
        self.pet.get_nome()
        self.opcoes_menu()

    def get_idade(self):
        self.pet.get_idade()
        self.opcoes_menu()

    def criar_pet(self):
        ...
    def opcoes_menu(self):
        print('\n O que você deseja fazer?')
        print('A) Alimentar o Pet')
        print('B) Brincar com o Pet')
        print('C) Ver Status')
        print('D) Verificar Nome')
        print('E) Verificar Idade')
        print('F) Criar outro Pet')
        opt = str(input('Qual opção você deseja: '))

        match opt.lower():
            case 'a':
                self.alimentar_pet()
            case 'b':
                self.brincar_pet()
            case 'c':
                self.get_status()
            case 'd':
                self.get_name()
            case 'e':
                self.get_idade()
            case 'f':
                self.criar_pet()
            case _:
                print('Opção Invalida')
                self.opcoes_menu() 


