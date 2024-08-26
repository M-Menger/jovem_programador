pais_a = 80000
taxa_a = 0.03
pais_b = 200000
taxa_b = 0.015
ano = 0

while pais_a < pais_b:
    pais_a += pais_a * taxa_a
    pais_b += pais_b * taxa_b

    ano += 1 

print(f'\nO pais A levara {ano} anos para superar os habitantes do pais B.\n')

