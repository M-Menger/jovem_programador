import customtkinter as CTk

def pega_horas():
    return float(hrs_trabalhadas.get())


def pega_valor():
    return float(vlr_hora.get())

def calcula_salario():
    valor_hora = pega_horas()
    horas_trabalhadas = pega_valor()

    salario_bruto = valor_hora*horas_trabalhadas

    fgts = salario_bruto * 0.11
    inss = salario_bruto * 0.10
    sindicato = salario_bruto * 0.03
    ir = 0
    if salario_bruto <= 900:
        total_desconto = salario_bruto * 0.13
    elif salario_bruto <= 1500:
        total_desconto = salario_bruto * 0.18
        ir = salario_bruto * 0.05
    elif salario_bruto <= 2500:
        total_desconto = salario_bruto * 0.23
        ir = salario_bruto * 0.10
    else:
        total_desconto = salario_bruto * 0.33
        ir = salario_bruto * 0.20

    salario_liquido = salario_bruto - total_desconto

    res1.configure(text=f'{salario_bruto:.2f}R$')
    res2.configure(text=f'{ir:.2f}R$')
    txt2.configure(text=f'(-) IR ({ir/salario_bruto*100:.0f} %):')
    res3.configure(text=f'{inss:.2f}R$')
    res4.configure(text=f'{sindicato:.2f}R$')
    res5.configure(text=f'{fgts:.2f}R$')
    res6.configure(text=f'{total_desconto:.2f}R$')
    res7.configure(text=f'{salario_liquido:.2f}R$')

window = CTk.CTk()
window.geometry('500x360')
window.title('JP Holerite')

vlr_hora = CTk.CTkEntry(window, placeholder_text='Valor Hora')
vlr_hora.place(relx=0.04, rely=0.15, anchor=CTk.W)

hrs_trabalhadas = CTk.CTkEntry(window, placeholder_text='Horas Trabalhadas')
hrs_trabalhadas.place(relx=0.5, rely=0.15, anchor=CTk.CENTER)

btn_gerar = CTk.CTkButton(window, text='Gerar Holerite', command=calcula_salario)
btn_gerar.place(relx=0.96, rely=0.15, anchor=CTk.E)

txt1 = CTk.CTkLabel(window, text='Salario Bruto:')
txt1.place(relx=0.48, rely=0.40, anchor=CTk.E)
res1 = CTk.CTkLabel(window, text='')
res1.place(relx=0.49, rely=0.40, anchor=CTk.W)

txt2 = CTk.CTkLabel(window, text='(-) IR (0%):')
txt2.place(relx=0.48, rely=0.50, anchor=CTk.E)
res2 = CTk.CTkLabel(window, text='')
res2.place(relx=0.49, rely=0.50, anchor=CTk.W)

txt3 = CTk.CTkLabel(window, text='(-) INSS (10%):')
txt3.place(relx=0.48, rely=0.57, anchor=CTk.E)
res3 = CTk.CTkLabel(window, text='')
res3.place(relx=0.49, rely=0.57, anchor=CTk.W)

txt4 = CTk.CTkLabel(window, text='(-) Sindicato (3%):')
txt4.place(relx=0.48, rely=0.64, anchor=CTk.E)
res4 = CTk.CTkLabel(window, text='')
res4.place(relx=0.49, rely=0.64, anchor=CTk.W)

txt5 = CTk.CTkLabel(window, text='FGTS (5%):')
txt5.place(relx=0.48, rely=0.71, anchor=CTk.E)
res5 = CTk.CTkLabel(window, text='')
res5.place(relx=0.49, rely=0.71, anchor=CTk.W)

txt6 = CTk.CTkLabel(window, text='Total Descontos:')
txt6.place(relx=0.48, rely=0.78, anchor=CTk.E)
res6 = CTk.CTkLabel(window, text='')
res6.place(relx=0.49, rely=0.78, anchor=CTk.W)

txt7 = CTk.CTkLabel(window, text='Salario Liquido:')
txt7.place(relx=0.48, rely=0.92, anchor=CTk.E)
res7 = CTk.CTkLabel(window, text='')
res7.place(relx=0.49, rely=0.92, anchor=CTk.W)

window.mainloop()
