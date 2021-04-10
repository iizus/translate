import PySimpleGUI as gui

title = 'Translate'
width = 80
height = 10
timeout = 100

box_size = (width, height)

def make_box(text, key):
	box = gui.Multiline(text, key=key, size=box_size)
	return box

# languages = ['choice 1', 'choice 2']

left_arrow = gui.Text('<-')
right_arrow = gui.Text('->')
arrow = right_arrow

def make_layout(text):
	layout = [
		[make_box(text, key='left_box'), arrow, make_box(text, key='right_box')]
	]
	return layout

text = ''
layout = make_layout(text)
window = gui.Window(title, layout)

while True:
	event, values = window.read(timeout=timeout)
	print(event, values)

	if event is None: break