#Professor confesso que nessa tive que apelar para IA, não consegui elaborar um código que retornasse
#de maneira correta os quadrados, tentei de diversas formas mas não cheguei em nenhuma solução, joguei
#o problema na IA solicitando que não usasse biblioteca externa, li, e entendi o código, porém os códigos
#que estava tentando fazer eram muito mais simples do que esse.
#Obs.: Para as demais questões usei somente documentação!

def is_quadrado_magico(quad):
    # Verificar a soma das linhas
    linha1 = quad[0] + quad[1] + quad[2]
    linha2 = quad[3] + quad[4] + quad[5]
    linha3 = quad[6] + quad[7] + quad[8]
    
    # Verificar a soma das colunas
    coluna1 = quad[0] + quad[3] + quad[6]
    coluna2 = quad[1] + quad[4] + quad[7]
    coluna3 = quad[2] + quad[5] + quad[8]
    
    # Verificar a soma das diagonais
    diagonal1 = quad[0] + quad[4] + quad[8]
    diagonal2 = quad[2] + quad[4] + quad[6]
    
    # Todas as somas devem ser iguais
    if (linha1 == linha2 == linha3 == coluna1 == coluna2 == coluna3 == diagonal1 == diagonal2):
        return True
    
    return False

def permutacoes(lista, l, r, quadrados_magicos):
    if l == r:
        if is_quadrado_magico(lista):
            quadrados_magicos.append(lista[:])
    else:
        for i in range(l, r + 1):
            lista[l], lista[i] = lista[i], lista[l]  # Swap
            permutacoes(lista, l + 1, r, quadrados_magicos)
            lista[l], lista[i] = lista[i], lista[l]  # Swap de volta

def exibir_quadrados_magicos():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    quadrados_magicos = []
    
    # Gerar todas as permutações possíveis
    permutacoes(numeros, 0, len(numeros) - 1, quadrados_magicos)
    
    # Exibir os quadrados mágicos
    for quad in quadrados_magicos:
        print(f"{quad[0]} {quad[1]} {quad[2]}")
        print(f"{quad[3]} {quad[4]} {quad[5]}")
        print(f"{quad[6]} {quad[7]} {quad[8]}")
        print()

# Executar a função para exibir os quadrados mágicos
exibir_quadrados_magicos()
