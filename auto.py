import pyautogui
from time import sleep
import os


path = r"C:\Users\Caio\Recursos\Documents\Programação\Python\Aplicação_cadastro_alunos\dist\gui.exe"
if os.path.exists(path):
    os.startfile(path)
else:
    print("O arquivo executável não foi encontrado.")

with open('alunos.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        sleep(1)
        # print(line.split(',')[0])
        # print(line.split(',')[1])
        aluno = line.split(',')[0]
        email = line.split(',')[1]
        pyautogui.click(351,340, duration=3)
        pyautogui.write(aluno)
        pyautogui.click(324,378, duration=3)
        pyautogui.write(email)
        pyautogui.click(363,399, duration=3)
        sleep(1)