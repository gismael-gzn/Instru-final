from tkinter import *
from PIL import ImageTk,Image

def test(root):
	img = Image.open('./icons/inicio.png')
	img = img.resize((120, 120), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	elem = Label(root, image=img)
	elem.pack()

def main():
	print('hello world')
	root = Tk()
	test(root)
	root.mainloop()

if __name__=='__main__':
	main()
