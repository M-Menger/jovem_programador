diaSem = ['domingo','segunda','terça','quarta','quinta','sexta','sábado']

diaEscolhido = input('Digite um dia da semana para saber quais faltam!\n')
indexDia = diaSem.index(diaEscolhido.lower())

print(diaSem[indexDia+1:])
