frase = str(input('Digite uma frase: ')).lower().split()

dicionario = {}

for palavra in frase:
   dicionario[palavra] = dicionario.get(palavra, 0)+1

print(dicionario)
