from tkinter import *
import tkinter
from PIL import ImageTk,Image
import sys,os

import gui

def clear_app_frame(program : gui.gui_program):
	for widgets in program.get_frame('app').winfo_children():
		widgets.destroy()

def inicio_fn(program : gui.gui_program):
	if program.get_state() == 'inicio':
		return
	clear_app_frame(program)

	img = program.get_ref('inicio_img')
	if not img:
		img = Image.open('./icons/inicio.png')
		img = img.resize((850, 700), Image.ANTIALIAS)
		img = ImageTk.PhotoImage(img)
		img = program.set_ref('inicio_img', img)

	elem = program.push_to_frame('app', Label, image=img)
	elem.pack()

	program.set_state('inicio')

def monitor_fn(program : gui.gui_program):
	if program.get_state() == 'monitor':
		return
	clear_app_frame(program)

	program.def_frame(program.get_frame('app'), 'Temp', text='Temp', 
	height=720, width=430).grid(row=0,column=0)
	program.get_frame('Temp').pack_propagate(False)
	program.get_frame('Temp').grid_propagate(False)

	program.def_frame(program.get_frame('app'), 'Light', text='Luz', 
	height=720, width=430).grid(row=0,column=1)
	program.get_frame('Light').pack_propagate(False)
	program.get_frame('Light').grid_propagate(False)

	frameCnt = 44
	frames = program.get_ref('temp-gif')
	if not frames:
		frames = [PhotoImage(file='./icons/term.gif', format='gif -index %i' %(i)) 
			for i in range(frameCnt)]
		program.set_ref('temp-gif', frames)

	program.push_to_frame('Temp', Label, image=frames[0]).pack()
	# while 1:
	# 	i = i % (frameCnt+1)
	# 	l.configure(text='hola')
	# 	l.pack()

	program.set_state('monitor')

def ayuda_fn(program : gui.gui_program):
	if program.get_state() == 'ayuda':
		return
	clear_app_frame(program)

	ref = program.push_to_frame('app', Label, text='Ayuda')
	ref.pack()

	program.set_state('ayuda')

def main():
	program = gui.gui_program(
		'Instru-Monitor', './icons/programico.png', (1080, 720),
		height=720, width=1080
		)
	program.get_frame('main').pack()
	program.get_frame('main').grid_propagate(False)
	program.root.resizable(False, False)

	program.def_frame(
		program.get_frame('main'), 'menu', text='Menu', height=720, width=200
		).grid(row=0, column=0)
	program.get_frame('menu').pack_propagate(False)
	program.get_frame('menu').grid_propagate(False)

	program.def_frame(
		program.get_frame('main'), 'app', text='App', height=720, width=880
		).grid(row=0, column=1)
	program.get_frame('app').pack_propagate(False)
	program.get_frame('app').grid_propagate(False)

	menu_strings = ['Inicio', 'Monitor', 'Ayuda', 'Salir']
	menu_functors = [
		lambda p=program: inicio_fn(p), lambda p=program: monitor_fn(p),
		lambda p=program: ayuda_fn(p), program.root.quit
		]
	pixel = tkinter.PhotoImage(width=1, height=1)
	for s,f in  zip(menu_strings, menu_functors):
		b = program.push_to_frame(
			'menu', Button, text=s, image=pixel, width=200/1.5, height=720/4.5, 
			compound='c', command=f
			)
		b.pack(side=TOP)
	inicio_fn(program)

	program.start_gui()

if __name__=="__main__":
	main()

