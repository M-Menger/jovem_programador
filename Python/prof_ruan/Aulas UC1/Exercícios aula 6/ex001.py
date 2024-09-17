rpt = True
saldo = 0.00

while(rpt == True):
  
    opt = input('Digite a opção desejada: \n(a).Consulta Saldo \n(b).Saque \n(c).Deposito \n(d).Sair.\n') 
    
    if(opt == 'a'):
        print(f'Saldo disponivel: R${saldo:.2f}.')

    elif(opt == 'b'):
        saque = float(input('Saque valor: R$'))

        if(saque > saldo):
            print('Valor indisponivel.\n')
        else:
            saldo -= saque

    elif(opt == 'c'):
        depos = float(input('Deposito valor: R$ '))
        saldo += depos

    elif(opt == 'd'):
        print('Sair')
        rpt = False
