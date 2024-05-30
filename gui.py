import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title('cadastro de Alunos')

# 1 - Criando tabela Treeview
tree = ttk.Treeview(root, columns=('Name', 'Email'))
tree.heading('Name', text='Name')
tree.heading('Email', text='Email')
tree.pack()



root.mainloop()