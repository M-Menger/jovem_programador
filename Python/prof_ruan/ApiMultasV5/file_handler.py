from pathlib import Path

def pegaAuto():
    diretorio = Path('C:/Users/Balcão/Desktop/Developing/ApiMultasV5/attachments/')
    lista_arquivos = list(diretorio.glob('*'))
    auto = [str(arquivo)[59:].replace('.pdf', '') for arquivo in lista_arquivos]
    return auto
