# Cadastro de Alunos
***
Este é um simples programa em Python que permite cadastrar alunos em uma interface gráfica usando Tkinter e também automatiza a inserção desses alunos em uma aplicação externa.

## Funcionalidades

- **Cadastro de Alunos**: Permite inserir o nome e o e-mail de um aluno e adicioná-lo à lista de alunos cadastrados.
- **Integração com Aplicação Externa**: Automatiza a inserção dos alunos em uma aplicação externa.

## Requisitos

Para executar este programa, é necessário ter Python instalado em seu computador. Além disso, certifique-se de ter os seguintes módulos Python instalados:
- tkinter
- pyautogui

## Instalação e Requisitos

Você pode instalar os requisitos usando o pip. Abra o terminal ou prompt de comando e execute o seguinte comando:

- pip install tkinter pyautogui

1. Baixe o código fonte para o seu computador.
2. Digite o código `pyinstaller --onefile gui.py` para gerar o executável
3. Troque o caminho do arquivo executável gerado, no trecho:
    ´´path = r"C:\Users\Caio\Recursos\Documents\Programação\Python\Aplicação_cadastro_alunos\dist\gui.exe"´´
4. Ajuste as coordenadas conforme a resolução do seu monitor, no trecho:
    ´´pyautogui.click(351,340, duration=3)
        pyautogui.write(aluno)
        pyautogui.click(324,378, duration=3)
        pyautogui.write(email)
        pyautogui.click(363,399, duration=3)´´´
5. Execute o código
