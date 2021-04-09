import PySimpleGUI as gui

title = 'Translate'
width = 80
height = 30

box_size = (width, height)
left_box = gui.Multiline(size=box_size)
right_box = gui.Multiline(size=box_size)

layout = [
    [left_box, right_box]
]

window = gui.Window(title, layout)

while True:
	event, values = window.read()
	if event is None: break