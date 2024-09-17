import customtkinter as CTk

def cadastrar_aluno():
    frameOpt = CTk.CTkFrame(master=window,
                                width=430,
                                height=200,
                                corner_radius=8)
    frameOpt.place(relx=0.31, rely=0.7, anchor=CTk.W)

    txtBox = CTk.CTkLabel(master=frameOpt,
                          text='Cadastro de aluno',)
    txtBox.place(relx=0.5, rely=0.2, anchor=CTk.CENTER)

    nome = CTk.CTkEntry(frameOpt, 
                        placeholder_text='Insira o nome do aluno aqui: ')
    nome.place(relx=0.5, rely=0.4,anchor=CTk.CENTER)

    turma = CTk.CTkEntry(frameOpt, 
                        placeholder_text='Insira a turma do aluno aqui: ')
    turma.place(relx=0.5, rely=0.6,anchor=CTk.CENTER)


def remover_aluno():
    frameOpt = CTk.CTkFrame(master=window,
                                width=430,
                                height=200,
                                corner_radius=8)
    frameOpt.place(relx=0.31, rely=0.7, anchor=CTk.W)

    txtBox = CTk.CTkLabel(master=frameOpt,
                          text='Boa noite!',)
    txtBox.place(relx=0.5, rely=0.5, anchor=CTk.CENTER)


def pagAluno():
    janPagAluno = CTk.CTkToplevel()
    janPagAluno.geometry('600x300')

    button = CTk.CTkButton(master=janPagAluno, corner_radius=10, text='Voltar', command=janPagAluno.destroy)
    button.place(relx=0.8, rely=0.9, anchor=CTk.CENTER)

    menuPagAluno = CTk.CTkFrame(master=janPagAluno,
                               width=180,
                               height=280,
                               corner_radius=8)
    menuPagAluno.place(relx=0.18, rely=0.5, anchor=CTk.CENTER)

    labelMenuALuno = CTk.CTkLabel(master=janPagAluno,
                                text= 'Menu',
                                width=120,
                                height=25,
                                corner_radius=8)
    labelMenuALuno.place(relx=0.08, rely=0.15, anchor=CTk.W)

    radioALuno = CTk.StringVar(value='other')

    menuRadio1 = CTk.CTkRadioButton(master=janPagAluno, text='Editar Nome', value='A', variable=radioALuno,command=abriMenu)
    menuRadio1.place(relx=0.08, rely=0.3, anchor=CTk.W)

    menuRadio2 = CTk.CTkRadioButton(master=janPagAluno, text='Editar Turma', value='B', variable=radioALuno, command=abriMenu)
    menuRadio2.place(relx=0.08, rely=0.4, anchor=CTk.W)

    menuRadio3 = CTk.CTkRadioButton(master=janPagAluno, text='Adicionar Nota', value='C', variable=radioALuno, command=abriMenu)
    menuRadio3.place(relx=0.08, rely=0.5, anchor=CTk.W)

    menuRadio4 = CTk.CTkRadioButton(master=janPagAluno, text='Adicionar Falta', value='E', variable=radioALuno, command=abriMenu)
    menuRadio4.place(relx=0.08, rely=0.6, anchor=CTk.W)

    menuRadio5 = CTk.CTkRadioButton(master=janPagAluno, text='Mostrar Média', value='F', variable=radioALuno, command=abriMenu)
    menuRadio5.place(relx=0.08, rely=0.7, anchor=CTk.W)

    menuRadio6 = CTk.CTkRadioButton(master=janPagAluno, text='Mostrar Notas', value='G', variable=radioALuno, command=abriMenu)
    menuRadio6.place(relx=0.08, rely=0.8, anchor=CTk.W)

    menuRadio7 = CTk.CTkRadioButton(master=janPagAluno, text='Mostrar Faltas', value='H', variable=radioALuno, command=abriMenu)
    menuRadio7.place(relx=0.08, rely=0.9, anchor=CTk.W)


def abriMenu():
    match radioVar.get():
        case 'A':
            cadastrar_aluno()
        case 'B':
            remover_aluno()
        case 'C':
            pagAluno()


window = CTk.CTk()  
window.geometry('640x360')
window.title('Sistema Alunos')
CTk.set_appearance_mode('dark')


frameAluno = CTk.CTkFrame(master=window,
                               width=620,
                               height=120,
                               corner_radius=8)
frameAluno.place(relx=0.5, rely=0.2, anchor=CTk.CENTER)

frameMenu = CTk.CTkFrame(master=window,
                               width=170,
                               height=200,
                               corner_radius=8)
frameMenu.place(relx=0.15, rely=0.7, anchor=CTk.CENTER)

radioVar = CTk.StringVar(value='other')

menuRadio1 = CTk.CTkRadioButton(master=frameMenu, text='Cadastrar Aluno', value='A', variable=radioVar,command=abriMenu)
menuRadio1.place(relx=0.2, rely=0.3, anchor=CTk.W)

menuRadio2 = CTk.CTkRadioButton(master=frameMenu, text='Remover Aluno', value='B', variable=radioVar, command=abriMenu)
menuRadio2.place(relx=0.2, rely=0.5, anchor=CTk.W)

menuRadio3 = CTk.CTkRadioButton(master=frameMenu, text='Pagina do Aluno', value='C', variable=radioVar, command=abriMenu)
menuRadio3.place(relx=0.2, rely=0.7, anchor=CTk.W)

labelAuto = CTk.CTkLabel(master=window,
                               text= 'Aqui irá aparecer o Frame com o Menu solicitado',
                               width=120,
                               height=25,
                               corner_radius=8)
labelAuto.place(relx=0.65, rely=0.7, anchor=CTk.CENTER)

label = CTk.CTkLabel(master=frameAluno,
                               text= '''Tabela de alunos ficara aqui''',
                               width=100,
                               height=100,
                               corner_radius=8)
label.place(relx=0.5, rely=0.5, anchor=CTk.CENTER)

window.mainloop()
