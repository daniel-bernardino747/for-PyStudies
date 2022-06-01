import PySimpleGUI as sg
"""layout = [
    [sg.Button('Botão 1'), sg.Button('Coluna 1')],  # Linha 1
    [sg.Button('Botão 2'), sg.Button('Coluna 1')],  # Linha 2
    [sg.Text('Aperte o botão 3: '), sg.Button('Botão 3'), sg.Button('Coluna 1')]   # Linha 3
]"""
layout = [
    [sg.Image(filename='logo-python.png')]
]

window = sg.Window(
    'Janela da Live de Python',
    layout=layout
)

window.read()

window.close()
