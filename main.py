import PySimpleGUI as gui

layout = [
    [gui.InputText(), gui.InputText()]
]

win = gui.Window('', layout)

while True:
  event, values = win.read()