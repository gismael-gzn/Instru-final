import sys,os
from tkinter import *

class gui_program(object):
	root : Tk
	frames : dict
	elems : dict
	perm_refs: dict
	sm_state : str

	def __init__(self, title: str, icon_path : str, xy : tuple, **kwargs):
		self.root = Tk()
		self.root.title(title)
		if(icon_path):
			self.root.iconphoto(True, PhotoImage(file=os.path.join(sys.path[0], icon_path)))
		self.elems = dict()
		self.frames = dict()
		self.perm_refs = dict()
		self.sm_state = ''

		self.root.geometry(f'{xy[0]}x{xy[1]}')

		self.frames['main'] = LabelFrame(self.root, kwargs)

		self.log(f'title:{title}, icon_path:{icon_path}, xy:{xy}, {kwargs}' + 
		f' {id(self.frames["main"])}')

	def def_elem(self, parent, name_id : str, ctor, **kwargs):
		self.elems[name_id] = ctor(parent, kwargs)
		return self.elems[name_id]

	def get_elem(self, name_id : str):
		if name_id in self.elems:
			return self.elems[name_id]
		return None

	def def_frame(self, parent, frame_id : str, **kwargs):
		self.frames[frame_id] = LabelFrame(parent, kwargs)
		return self.frames[frame_id]

	def get_frame(self, frame_id : str):
		return self.frames[frame_id]

	def push_elem(self, parent, ctor, **kwargs):
		return ctor(parent, kwargs)

	def push_to_frame(self, frame_id : str, ctor, **kwargs):
		return ctor(self.get_frame(frame_id), kwargs)

	def set_ref(self, key : str, obj : object):
		self.perm_refs[key] = obj
		return self.perm_refs[key]
	
	def get_ref(self, key : str):
		if key in self.perm_refs:
			return self.perm_refs[key]
		return None

	def set_state(self, state : str):
		self.sm_state = state
		return self.sm_state

	def get_state(self):
		return self.sm_state

	def start_gui(self):
		self.root.mainloop()

	def log(self, string : str):
		print(string)
