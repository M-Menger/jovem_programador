regulamento = 50
peso = float(input('Qual o peso total pescado: ')) 
valor = 4.00

excesso = peso - regulamento

if peso > regulamento:
    multa = excesso * 4.00
    print(f'Você excedeu {excesso:.2f}Kgs do limite regulamentado, a multa é de: {multa:.2f}R$')
else:
    print('Multa não Aplicavel!')
    