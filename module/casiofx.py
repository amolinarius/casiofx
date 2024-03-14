import tkinter.messagebox as messagebox
import tkinter.simpledialog as simpledialog
from decimal import Decimal as D
from random import randint
from tkinter import *
import threading
import turtle
import time

class Settings():
	def __init__(self):
		self.limitedcomments = True # Whether or not the comments are limited to "Yes"|"No"|"Result: "|"Number? "
		self.debugMode = True # Whether or not send debug messages to the console
		self.instantDraw = False # Whether or not the graphics are instantly drawn. NOT WORKING
SETTINGS = Settings()

class InvalidCommentError(Exception): pass

class Calculator():
	def __init__(self, title="Casio Fx92+ College", ratio=4):
		self.RATIO = ratio
		self.WIDTH = 192.5*self.RATIO
		self.HEIGHT = 50*self.RATIO
		self.mainloop = mainloop
		self.x = 0
		self.y = 0
		self.angle = 0
		self.title = title
		WIDTH = self.WIDTH
		HEIGHT = self.HEIGHT
		self.app = Tk(title)
		self.app.geometry(f'{int(WIDTH)}x{HEIGHT}')
		self.app.resizable(False, False)
		cnv = Canvas(self.app, width=WIDTH, height=HEIGHT)
		cnv.pack()
		self.t = turtle.RawTurtle(cnv)
		self.penup()
		if SETTINGS.instantDraw: turtle.tracer(0, 0)

	def _update(self):
		self.x = self.t.position()[0]/4
		self.y = self.t.position()[1]/4
		# turtle.update()
	def forward(self, pixels): 
		self.t.forward(pixels*self.RATIO)
		self._update()
	def rotate(self, angle):
		self.t.left(angle)
		self._update()
	def goto(self, x, y):
		self.t.goto(x*self.RATIO, y*self.RATIO)
		self._update()
	def penup(self): self.t.penup()
	def pendown(self): self.t.pendown()
	def stop(self): self.app.destroy()
	def wait(self): time.sleep(5) # should enhance that
	def lookat(self, angle):
		self.t.setheading(angle)
		self.angle = angle
		self._update()
	def comment(self, _text: str):
		ALLOWED_TEXTS = ['Yes', 'No', 'Result: ', 'Number? ']
		FORMATTED_TEXTS = [t.lower().strip() for t in ALLOWED_TEXTS]
		if SETTINGS.limitedcomments:
			if FORMATTED_TEXTS.__contains__(_text.lower().strip()): text = ALLOWED_TEXTS[FORMATTED_TEXTS.index(_text.lower().strip())]
			else: raise InvalidCommentError()
		else: text = _text
		messagebox.showinfo(f'Comment - {self.title}', text)
		if SETTINGS.debugMode: print('Commented: ', text)
	def displayResult(self, _result):
		if type(_result) == float or type(_result) == int:
			messagebox.showinfo(f'Result Display - {self.title}', _result)
			if SETTINGS.debugMode: print('Displayed result: ', _result)
		else: raise InvalidCommentError()
	def askValue(self, var: str):
		prompt = var.upper()+'? '
		value = None
		while value == None: value = simpledialog.askfloat(prompt, prompt)
		
		if SETTINGS.debugMode: print(f'Found value {value} for variable {var.upper()}')
		return value

	def asyncMainloop(self):
		thread = threading.Thread(target=mainloop)
		thread.run()

def RanInt(a, b): 
	# Creates a random integer between a and b
	return randint(a, b)

def Ent(number: float):
	# Returns the integer part of the argument
	return round(number, 1) // 1 # Rounds to prevent unexact numbers (e.g. 1.2 being 1.9999999...)

print('Successfully created Calculator class & utils')