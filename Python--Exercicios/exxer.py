import PySimpleGUI as sg
import random
layout = [
    [sg.Text('usuario')],
    [sg.Input()],
    [sg.Text('senha')],
    [sg.Input()],
    [sg.Button('login')],
    [sg.Text("", key='mensagem')],

]

window = sg.Window('login', layout=layout)

while True:
    event, volues = window.read()
    if event == sg.WIN_CLOSED:
        Break

