def maiorIdade(idade):
    if idade >= 18:
        res = True
    else:
        res = False
    return res


idade = int(input('Digite a sua idade: '))
print(maiorIdade(idade))