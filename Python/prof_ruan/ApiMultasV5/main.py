from file_handler import pegaAuto
from excel_handler import searchAIT, pegaDados, pegaValor, pegaDestino, endProccess
from email_handler import sendMail
import win32com.client as win32
import customtkinter as CTk
from tkinter import ttk


def gerar_lista(treeAutos):
    lista = pegaAuto()

    if 'desktop.ini' in lista:
        lista.remove('desktop.ini')

    for i in lista:
        resSearch = searchAIT(i)
        resDados = pegaDados(resSearch)
        resValor = pegaValor(resDados[2])
        resDestino = pegaDestino(resDados[0])

        listaAutos = []
        dadosAuto = {
            'Auto':i,
            'Placa':resDados[0],
            'Valor':resValor,
            'Responsavel':resDestino
        }

        listaAutos.append(dadosAuto)
        treeAutos.insert("", "end", values=(dadosAuto['Auto'], dadosAuto['Placa'], f'{dadosAuto['Valor']}R$',dadosAuto['Responsavel']))


def main(treeAutos):
    lista = pegaAuto()

    if 'desktop.ini' in lista:
        lista.remove('desktop.ini')

    for i in lista:
        resSearch = searchAIT(i)
        resDados = pegaDados(resSearch)
        resValor = pegaValor(resDados[2])
        resDestino = pegaDestino(resDados[0])

        listaAutos = []
        dadosAuto = {
            'Auto':i,
            'Placa':resDados[0],
            'Valor':resValor,
            'Responsavel':resDestino
        }

        listaAutos.append(dadosAuto)
        treeAutos.insert("", "end", values=(dadosAuto['Auto'], dadosAuto['Placa'], f'{dadosAuto['Valor']}R$',dadosAuto['Responsavel']))

        caminho = f'C:/Users/Balcão/Desktop/Developing/ApiMultasV5/attachments/{i}.pdf'
        img_path = 'C:/Users/Balcão/Desktop/EQS_Engenharia/9.Diversos/assinatura.png'

        subject = f'ALERTA: Indicação de Condutor, placa {resDados[0]} auto de infração {i}'

        body = f'''
            <p>Venho através deste notificar o Auto de infração n° {i} Cometido com o veículo placa {resDados[0]}, no dia {resDados[1]} no valor de {resValor*0.8:.2f}R$,</p>
            <p>Por {resDados[3]}, infração cometida em {resDados[4]} na cidade de {resDados[5]}. </p>

            <p>FAVOR ENVIAR PRIMEIRAMENTE A CNH DO INFRATOR (PREFERENCIALMENTE O ARQUIVO DIGITAL) PARA QUE EU POSSA GERAR O TERMO EM SEU NOME E ENVIAR PARA ASSINATURA.</p>
            
            <p style=background-color:yellow;>O ANEXO ENVIADO NESTE E-MAIL NÃO É NECESSÁRIO PREENCHIMENTO. FOI ENVIADO APENAS PARA O COLABORADOR TER CIÊNCIA DA INFRAÇÃO.</p>
            <p style=background-color:yellow;> O DOCUMENTO QUE NECESSITA ASSINATURA, SERÁ ENVIADO POSTERIORMENTE, APÓS RECEBERMOS A CNH DO INFRATOR </p>

            <img src={img_path} alt="assinatura" width="500" height="120">
        '''

        envio = sendMail(resDestino, caminho, i, subject, body)
        endProccess(envio, i)

        return subject,body


if __name__ == '__main__':
    main()
