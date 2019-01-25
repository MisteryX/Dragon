#! /usr/bin/python3
# -*- coding: utf8 -*-
__author__ = "Maxim Morskov"
__copyright__ = "Copyright 2019, Maxim Morskov"
__credits__ = ["Maxim Morskov"]
__maintainer__ = "Maxim Morskov"

import tkinter


class Field:
	__height = None
	__width = None
	__rootWidget = None
	__canvas = None

	def __init__(self, height, width, **options):

		self.__rootWidget = tkinter.Tk()
		self.__height = height
		self.__width = width
		self.__options = options
		self.__canvas = tkinter.Canvas(self.__rootWidget, **options)
		self.__canvas.pack()
		self.__rootWidget.mainloop()
