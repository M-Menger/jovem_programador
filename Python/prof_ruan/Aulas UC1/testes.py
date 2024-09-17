dicionario = {
    'nome':'Matheus',
    'sobrenome': 'Menger'
}

for i in dicionario:
    dicionario['sobrenome'] = dicionario.get('Menger', 'existe')

print(dicionario)