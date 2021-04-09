import PySimpleGUI as gui

title = 'Translate'
width = 80
height = 30

box_size = (width, height)

def make_box():
	box = gui.Multiline(size=box_size)
	return box

layout = [
    [make_box(), make_box()]
]

window = gui.Window(title, layout)

while True:
	event, values = window.read()
	if event is None: break