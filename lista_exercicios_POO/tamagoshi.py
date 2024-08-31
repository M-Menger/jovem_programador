from random import randint

class Tamagoshi:
    def __init__(self, nome, idade):
        self.nome = nome
        self.fome = randint(20,80)
        self.idade = idade
        self.humor = randint(20,80)

    
    def get_nome(self):
        print(self.nome)
    
    
    def get_idade(self):
        print(self.idade)
    

    def set_alimentar(self,alimento):
        if alimento == 'Ração':
            self.fome += 10
            self.humor -= 5
        else:
            self.fome += 5
            self.humor += 2

        print('Nham, Nham! Vamos comer!')


    def set_brincar(self, brincadeira):

        if brincadeira == 'Pega bolinha':
            self.humor += 15
            self.fome -= 7
        else:
            self.humor += 10

        print('Vamos brincar! Ihuul!')


    def get_fome(self):
        if self.fome <= 0:
            msg_fome = f'{self.fome}% Morreu de fome!'
        elif self.fome <= 25:
            msg_fome = f'{self.fome}% Desnutrido!'
        elif self.fome <= 50:
            msg_fome = f'{self.fome}% Fome!'
        elif self.fome <= 80:
            msg_fome = f'{self.fome}% Satisfeito!'
        elif self.fome < 100:
            msg_fome = f'{self.fome}% Quase explodindo de comer!'
        else:
            msg_fome = f'{self.fome}% Explodiu e morreu!'

        return print(msg_fome)


    def get_humor(self):
        if self.humor <= 0 or self.humor >= 100: 
            msg_humor = f'{self.humor}% Depressão bateu, Morreu!'
        elif self.humor <= 25:
            msg_humor = f'{self.humor}% Deprimido!'
        elif self.humor <= 50:
            msg_humor = f'{self.humor}% Alegre!'
        elif self.humor <= 80:
            msg_humor =  f'{self.humor}% Feliz!'
        elif self.humor < 100:
            msg_humor = f'{self.humor}% Eufórico!'
        else:
            msg_humor =  f'{self.humor}% Morreu de felicidade!'

        return print(msg_humor)
    
    