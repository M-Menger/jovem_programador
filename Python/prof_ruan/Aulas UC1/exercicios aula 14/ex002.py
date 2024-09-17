def menu():
    print('-'*10)
    print('   Menu   ')
    print('-'*10)
    ('\nEscolha uma opção: ')
    print('(a) Consulta Saldo')
    print('(b) Saque e')
    print('(c) Deposito e')
    a = input('(d) Sair \n')
    
    return a


def opcao(res):
    a = res.lower()
    if a == 'a':
        print('Opção escolhida (a).Consulta Saldo')
    elif a == 'b':
        print('Opção escolhida (b).Saque e')
    elif a == 'c':
        print('Opção escolhida (c).Deposito e')
    elif a == 'd':
        print('Opção escolhida (d).Sair')


res = menu()
opcao(res)


