import pyautogui
from time import sleep
import os

path = "C:\Users\Caio\Recursos\Documents\Programação\Python\Aplicação_cadastro_alunos\dist\gui.exe"


with open('alunos.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        # print(line.split(',')[0])
        # print(line.split(',')[1])
        aluno = line.split(',')[0]
        email = line.split(',')[1]
        if os.path.exists(path):
            os.startfile(path)
        else:
            print("O arquivo executável não foi encontrado.")
        
        