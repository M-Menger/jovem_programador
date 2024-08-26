def calcula_tempo():
        
        pais_a = float(input('Digite a população atual do pais A: \n'))
        taxa_a = float(input('Digite a taxa de crescimento anual: \n'))
        pais_b = float(input('Digite a população atual do pais B: \n'))
        taxa_b = float(input('Digite a taxa de crescimento anual: \n'))

        if pais_a > pais_b:
            print('O pais A já possui mais habitantes que o pais B!')
        elif pais_a <= pais_b and taxa_a < taxa_b:
            print('O pais A não conseguirá ser maior que o pais B!')
        else:

            ano = 0
            taxa_a = taxa_a/100
            taxa_b = taxa_b/100
            while pais_a < pais_b:
                pais_a += pais_a * taxa_a
                pais_b += pais_b * taxa_b

                ano += 1 

            print(f'\nO pais A levara {ano} anos para superar os habitantes do pais B.\n')


calcula_tempo()

while True:
    repetir = str(input('\nVocê deseja calcular novamente? (S/N): \n')).strip().lower()

    if repetir == 'n':
        break
    elif repetir == 's':
        print('\nVocê escolheu continuar.\n')
        calcula_tempo()
    else:
        print("Resposta inválida, por favor digite 's' para sim ou 'n' para não.")
