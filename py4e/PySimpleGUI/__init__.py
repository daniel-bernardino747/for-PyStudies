import PySimpleGUI as sg

layout = [
    [sg.Text('Hello from PySimpleGUI')],
    [sg.Button('OK')]
]

window = sg.Window('Demo', layout)

while True:
    event, values = window.read()
    if event == 'OK' or event == sg.WINDOW_CLOSED:
        break

window.close()
# sg.Window(title='Hello World', layout=[[]], margins=(300, 150)).read()
