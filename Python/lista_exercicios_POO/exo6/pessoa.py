class Pessoa():
    def __init__(self, nome, cpf, nascimento) -> None:
        self.nome = nome 
        self.cpf = cpf
        self.nascimento = nascimento

    def get_idade(self):
        ...
