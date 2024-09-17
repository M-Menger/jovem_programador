def pegaDados():
    vlr1 = int(input('Defina a quantidade de números entre inicio e fim da lista: '))
    vlr2 = int(input('Digite o valor inicial da lista: '))
    vlr3 = int(input('Digite o valor final da lista: '))

    return vlr1, vlr2, vlr3


def gera_lista_aleatoria(n, inferior, superior):
    lista = []
    vlr1 = superior - inferior
    vlr2 = vlr1/n
    print(vlr2)
    print(inferior)
    while inferior < superior:
        lista.append(inferior)
        inferior += n
    
    print(lista)


dados = pegaDados()

n = dados[0]
i = dados[1]
f = dados[2]

gera_lista_aleatoria(n, i, f)
