import tkinter as tk
from tkinter import ttk

def populate_tree(tree, data_dict):
    # Limpa os itens existentes na treeview
    for item in tree.get_children():
        tree.delete(item)
    
    # Adiciona os dados do dicionário à treeview
    for i in range(len(data_dict['nome'])):
        nome = data_dict['nome'][i]
        turma = data_dict['turma'][i]
        notas = ', '.join(map(str, data_dict['notas'][i]))
        faltas = data_dict['faltas'][i]
        tree.insert('', 'end', text=nome, values=(turma, notas, faltas))
        
def main():
    # Criando a janela principal
    root = tk.Tk()
    root.title("TreeView com Dados de um Dicionário")
    
    # Criando a Treeview
    tree = ttk.Treeview(root)
    tree.pack(expand=True, fill='both')
    tree["columns"] = ("Turma", "Notas", "Faltas")
    tree.heading('#0', text='Nome')
    tree.heading('Turma', text='Turma')
    tree.heading('Notas', text='Notas')
    tree.heading('Faltas', text='Faltas')
    
    # Dados do dicionário
    alunos = {
        "nome": ['Matheeus','Marcos','David','Felipe'], 
        "turma": [1, 2, 3, 4],
        "notas": [[9.5, 8.2, 7.1],[8.4, 9.1, 7.5],[7.4, 8.1, 9.5],[9.4, 6.1, 3.5]], 
        "faltas": [5,4,2,0]
    }
    
    # Preenchendo a Treeview com os dados do dicionário
    populate_tree(tree, alunos)
    
    root.mainloop()

if __name__ == "__main__":
    main()
