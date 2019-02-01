#! /usr/bin/python3
# -*- coding: utf8 -*-
__author__ = "Maxim Morskov"
__copyright__ = "Copyright 2019, Maxim Morskov"
__credits__ = ["Maxim Morskov"]
__maintainer__ = "Maxim Morskov"

import tkinter
from game import Game


class Scene:
	__height = None
	__width = None
	__options = None
	__rootWidget = None
	__canvas = None
	__game = None

	def __init__(self, game: Game, **options):

		self.__game = game
		self.__height = options.get('height', 0)
		self.__width = options.get('width', 0)
		self.__options = options

		self.__rootWidget = tkinter.Tk()
		self.__canvas = tkinter.Canvas(self.__rootWidget, **options)
		self.__canvas.pack()
		self.__set_event_handlers()

		self.__rootWidget.mainloop()

	def get_game(self)->Game:
		return self.__game

	def get_option(self, name: str):
		return self.__options.get(name, None)

	def __set_event_handlers(self):
		self.__rootWidget.bind('<Up><Down><Left><Right><Escape>', self.__dispatch_keyboard_event)

	def draw_sprite(self, X_cord: int, Y_cord: int, file_name: str):
		sprite = tkinter.PhotoImage(file=file_name)
		return self.__canvas.create_image(X_cord, Y_cord, image=sprite)

	def update(self):
		pass

	def __dispatch_keyboard_event(self, event):
		if 'Escape' == repr(event.keysym):
			self.__rootWidget.destroy()
		elif 'Up' == repr(event.keysym) or 'Down' == repr(event.keysym) or 'Right' == repr(event.keysym) or 'Left' == repr(event.keysym):
			self.get_game().get_player().set_direction(repr(event.keysym))
