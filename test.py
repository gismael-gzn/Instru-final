from tkinter import *
from PIL import ImageTk,Image

def test(root):
	img = Image.open('./icons/inicio.png')
	img = img.resize((120, 120), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	elem = Label(root, image=img)
	elem.pack()

def write_nums():
	fp = open('nums.txt', 'w')
	for i in range(255, 0, -1):
		fp.write(f'{i}\n')
	fp.close()

def main():
	write_nums()
	print('hello world')
	root = Tk()
	test(root)
	root.mainloop()

if __name__=='__main__':
	main()
