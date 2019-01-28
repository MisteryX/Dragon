#! /usr/bin/python3
# -*- coding: utf8 -*-
__author__ = "Maxim Morskov"
__copyright__ = "Copyright 2019, Maxim Morskov"
__credits__ = ["Maxim Morskov"]
__maintainer__ = "Maxim Morskov"

import tkinter


class Field:
	__options = None
	__rootWidget = None
	__canvas = None

	def __init__(self, **options):

		self.__rootWidget = tkinter.Tk()
		self.__options = options
		self.__canvas = tkinter.Canvas(self.__rootWidget, **options)
		self.__canvas.pack()
		self.__rootWidget.mainloop()

	def _draw_sprite(self, X_cord: int, Y_cord: int, file_name: str):
		sprite = tkinter.PhotoImage(file=file_name)
		return self.__canvas.create_image(X_cord, Y_cord, image=sprite)

	def draw_scene(self):
		pass
