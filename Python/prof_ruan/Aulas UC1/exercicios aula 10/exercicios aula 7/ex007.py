validaNome = ''
validaIdade = 200 

for i in range (0,10):
    nome = str(input(f'Digite o {i+1}° nome: '))
    idade = int(input(f'Digite a {i+1}° idade: '))
    if idade < validaIdade:
        validaIdade = idade
        validaNome = nome
print(f'O mais novo é {validaNome} com {validaIdade} anos')
