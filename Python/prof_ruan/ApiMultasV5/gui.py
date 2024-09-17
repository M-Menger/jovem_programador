import customtkinter as CTk
from tkinter import ttk
from main import gerar_lista, main

windowMaster = CTk.CTk()
windowMaster.geometry('640x360')
windowMaster.title('Envio de Multas v4.0')
CTk.set_appearance_mode('dark')

frameTree = CTk.CTkFrame(master=windowMaster,
                               width=620,
                               height=240,
                               corner_radius=8)
frameTree.place(relx=0.5, rely=0.36, anchor=CTk.CENTER)

treeAutos = ttk.Treeview(master=frameTree, columns=('AUTO','Placa','Valor','Responsável'), show='headings',height=5)

treeAutos.heading('AUTO', text='AUTO')
treeAutos.heading('Placa', text='Placa')
treeAutos.heading('Valor', text='Valor')
treeAutos.heading('Responsável', text='Responsável')

treeAutos.column('AUTO', width=100)
treeAutos.column('Placa', width=75)
treeAutos.column('Valor', width=70)
treeAutos.column('Responsável', width=250)

treeAutos.pack(side='left', fill='both', expand=True)

treeScroll = ttk.Scrollbar(master=frameTree, command=treeAutos.yview)
treeScroll.pack(side='right', fill='y')

treeAutos.config(yscrollcommand=treeAutos.set)

frameBtns = CTk.CTkFrame(master=windowMaster,
                               width=420,
                               height=110,
                               corner_radius=8)
frameBtns.place(relx=0.5, rely=0.85, anchor=CTk.CENTER)

btnEnviar = CTk.CTkButton(master=frameBtns, text='Enviar Auto',command=lambda: main(treeAutos))
btnEnviar.place(relx=0.5, rely=0.85, anchor=CTk.CENTER)

btnGerar = CTk.CTkButton(master=frameBtns, text='Envio Manual',command=lambda: main(treeAutos))
btnGerar.place(relx=0.5, rely=0.5, anchor=CTk.CENTER)

btnGerar = CTk.CTkButton(master=frameBtns, text='Gerar lista',command=lambda: gerar_lista(treeAutos))
btnGerar.place(relx=0.5, rely=0.15, anchor=CTk.CENTER)

windowMaster.mainloop()

