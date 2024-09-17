Api Multas

Aplicativo com objetivo de automatizar processo, obtendo assim ganho de tempo,
melhorando a produtividade.

O mesmo realiza a busca de dados referentes a infrações solicitadas pelo usuario,
na planilha de relatório geral de multas, com alguns acréscimos que fiz, como a
identificação do gestor de cada frota, e dados da multa.

Bibliotecas Utilizadas

openpyxl: Biblioteca utilizada para manipulação de arquivos Excel.
datetime: Biblioteca para manipulação de datas e horas.
pathlib.Path: Biblioteca para manipulação de caminhos de arquivos.
smtplib: Biblioteca para envio de emails usando o protocolo SMTP.
email.mime: Biblioteca para criação e manipulação de conteúdos de email (texto, anexo, etc).

Variáveis Globais

server_smtp: Endereço do servidor SMTP.
port: Porta para conexão com o servidor SMTP.
sender_mail: Email do remetente.
password: Senha do email do remetente.
lista: Lista inicializada vazia para armazenar dados dos arquivos.

Funções

pegaAuto()
    Descrição: Coleta todos os arquivos PDF de um diretório específico e extrai seus nomes sem a extensão.
    Retorno: Lista de nomes dos arquivos (sem extensão).

searchAIT(auto)
    Descrição: Procura o auto de infração na planilha 'DBMultas' e retorna o número da linha onde ele foi encontrado.
    Parâmetros: auto (string) - Número do auto de infração a ser pesquisado.
    Retorno: Número da linha onde o auto foi encontrado.

pegaDados(numCell)
Descrição: Coleta dados específicos (idCar, data, cod, infr, cep, city) da linha fornecida na planilha 'DBMultas'.
Parâmetros: numCell (int) - Número da linha de onde os dados serão extraídos.
Retorno: Uma tupla com os dados coletados.

pegaValor(cod)
Descrição: Procura o valor da multa na planilha 'CTB' usando o código fornecido.
Parâmetros: cod (string) - Código da infração.
Retorno: Valor da multa.

pegaDestino(placa)
Descrição: Procura o email do destinatário na planilha 'Destinatario' usando a placa fornecida.
Parâmetros: placa (string) - Placa do veículo.
Retorno: Email do destinatário.

sendMail(mail, caminho, auto)
Descrição: Envia um email com um anexo específico para o destinatário.
Parâmetros:
mail (string) - Email do destinatário.
caminho (string) - Caminho do arquivo a ser anexado.
auto (string) - Número do auto de infração (usado para nomear o anexo).
Retorno: Data e hora em que o email foi enviado.

endProccess(data, auto)
Descrição: Registra o envio do email na planilha 'LogEnvio'.
Parâmetros:
data (datetime) - Data e hora do envio do email.
auto (string) - Número do auto de infração.

Main

Obtenção dos arquivos:

A função pegaAuto é chamada para listar todos os arquivos PDF do diretório especificado.

Processamento dos autos:

Para cada auto na lista, as seguintes operações são realizadas:
Busca do auto na planilha 'DBMultas' usando searchAIT.
Coleta de dados adicionais da linha correspondente com pegaDados.
Coleta do valor da multa com pegaValor.
Coleta do email do destinatário com pegaDestino.

Preparação do email:

Define-se o assunto e o corpo do email com base nos dados coletados.

Envio do email:

O email é enviado usando a função sendMail.

Registro do envio:

O envio é registrado na planilha 'LogEnvio' com endProccess.