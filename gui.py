import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title('cadastro de Alunos')

# 1 - Criando tabela Treeview
tree = ttk.Treeview(root, columns=('Name', 'Email'))
tree.heading('Name', text='Name')
tree.heading('Email', text='Email')
tree.pack()

#  Criando os campos

label_name = tk.Label(root, text='Name')
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()

label_email = tk.Label(root, text='Email')
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()


# Botão para adicionar User
butto_add = tk.Button(root, text='Adicionar Aluno')
butto_add.pack()


root.mainloop()