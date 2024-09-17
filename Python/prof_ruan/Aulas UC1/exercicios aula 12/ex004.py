res = 'sim'
listaAnimais = []

while (res == 'sim'):
    listaAnimais.append(str(input('Digite o animal: ')))
    res = input('você deseja adicionar um animal? sim/não \n')

animais = ", ".join(listaAnimais)

print(animais)
