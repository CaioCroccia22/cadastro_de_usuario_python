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

## Instalação dos Requisitos

Você pode instalar os requisitos usando o pip. Abra o terminal ou prompt de comando e execute o seguinte comando:

> pip install tkinter pyautogui

## Como usar

1. Baixe o código fonte para o seu computador.
2. Abra o terminal ou prompt de comando e navegue até o diretório onde o código fonte está localizado.
3. Execute o programa digitando `python gui.py --onefile` para gerar o executável.
4. Troque o caminho no trecho: 
    > ``path = r"C:\Users\Caio\Recursos\Documents\Programação\Python\Aplicação_cadastro_alunos\dist\gui.exe"`
5. Abra o terminal ou o prompt de comando e execute:
    - python 
    - from mouseinfo import mouseInfo
    - mouseInfo()
6. Verifique as coordenadas e troque no trecho a seguir:
    > ``pyautogui.click(351,340, duration=3)
       pyautogui.write(aluno)
       pyautogui.click(324,378, duration=3)
       pyautogui.write(email)
       pyautogui.click(363,399, duration=3)`
7. Abra o terminal ou prompt de comando e navegue até o diretório onde o código fonte está localizado.
8. Execute:
    - `python auto.py`

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licensa
Este projeto é licenciado sob a MIT License.