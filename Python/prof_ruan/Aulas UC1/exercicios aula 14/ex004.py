def pegaDados():
    peso = float(input('Qual seu peso: '))
    altura = float(input('Qual sua altura: '))

    return peso,altura


def calcImc(peso,altura):
    imc = peso/(altura*altura)

    return imc


dados = pegaDados()
peso = dados[0]
altura = dados[1]
imc = calcImc(peso,altura)

print(f'{imc:.2f}')
