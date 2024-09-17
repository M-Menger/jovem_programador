import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import win32com.client as win32

server_smtp = 'smtp.office365.com'
port = 587
sender_mail = 'matheusmenger@movida.com.br'
mailPass = '6124067908.Mgr'
sendCC = 'frota@eqsengenharia.com.br'
ccCaique = 'caique@eqsengenharia.com.br'
teste = 'matheus-menger@hotmail.com'
teste2 = 'rootsl4bel@gmail.com'
provMail = 'matheus-menger@outlook.com'
provPass = 'Amr.6124067908'


def sendMail(mail, caminho, auto, subject, body):
    message = MIMEMultipart()
    message['From'] = provMail
    message['To'] = sender_mail
    message['Cc'] = sender_mail
    message['Subject'] = subject

    attachment = open(caminho, 'rb')

    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attachment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition', f'attachment; filename= {auto}.pdf')

    attachment.close()
    message.attach(att)

    message.attach(MIMEText(body, 'HTML'))

    try:
        server = smtplib.SMTP(server_smtp, port)
        server.starttls()

        server.login(provMail,provPass)
        #server.sendmail(provMail, (mail,sendCC, ccCaique,sender_mail), message.as_string())
        server.sendmail(provMail, sender_mail, message.as_string())
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print(f'Houve um erro: {e}')
    finally:
        server.quit()

    timeSend = datetime.now()

    return timeSend
