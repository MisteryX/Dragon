#! /usr/bin/python3
# -*- coding: utf8 -*-
__author__ = "Maxim Morskov"
__copyright__ = "Copyright 2019, Maxim Morskov"
__credits__ = ["Maxim Morskov"]
__maintainer__ = "Maxim Morskov"

import tkinter
from components.game_object import GameObject
from components.dragon import Dragon
from components.gold_coin import GoldCoin


class Scene:
	__height = None
	__width = None
	__options = None
	__rootWidget = None
	__canvas = None
	__objects = None
	__player = None

	BORDER_COLLISION_LEFT = 1
	BORDER_COLLISION_RIGHT = 2
	BORDER_COLLISION_TOP = 3
	BORDER_COLLISION_BOTTOM = 4

	def __init__(self, **options):

		self.__height = options.get('height', 0)
		self.__width = options.get('width', 0)
		self.__options = options

		self.__rootWidget = tkinter.Tk()
		self.__canvas = tkinter.Canvas(self.__rootWidget, **options)
		self.__canvas.pack()
		self.__set_event_handlers()

		self.__rootWidget.mainloop()

	def __init_objects(self):
		self.__objects = []
		self.__player = Dragon(self, self.get_option('player'), True)
		self.__objects.append(self.__player)
		self.__objects.append(GoldCoin(self))

	def get_width(self):
		return self.__width

	def get_height(self):
		return self.__height

	def get_option(self, name: str):
		return self.__options.get(name, None)

	def get_player(self)->Dragon:
		return self.__player

	def get_objects(self)->list:
		return self.__objects

	def __set_event_handlers(self):
		self.__rootWidget.bind('<Up><Down><Left><Right><Escape>', self.__dispatch_keyboard_event)

	def draw_sprite(self, X_cord: int, Y_cord: int, file_name: str):
		sprite = tkinter.PhotoImage(file=file_name)
		return self.__canvas.create_image(X_cord, Y_cord, image=sprite)

	def get_border_collisions(self, a_object: GameObject)->tuple:
		X, Y = a_object.get_next_position()
		result = []

		if (X - a_object.get_width() / 2) < 0:
			result.append(Scene.BORDER_COLLISION_LEFT)
		elif (X + a_object.get_width() / 2) > self.get_width():
			result.append(Scene.BORDER_COLLISION_RIGHT)

		if (Y - a_object.get_height() / 2) < 0:
			result.append(Scene.BORDER_COLLISION_TOP)
		elif (Y + a_object.get_height() / 2) > self.get_height():
			result.append(Scene.BORDER_COLLISION_BOTTOM)
		return tuple(result)

	def is_processing_of_border_collisions_successful(self, a_object: GameObject, a_collisions: tuple)->bool:
		pass

	def is_processing_of_objects_collisions_successful(self)->bool:
		pass

	def update(self)->bool:
		result = self.is_processing_of_objects_collisions_successful()
		if not result:
			return result

		for _object in self.get_objects():
			result = self.is_processing_of_border_collisions_successful(_object, self.get_border_collisions(_object))
			if not result:
				return result

			_object.move()
			_object.draw()
		return True

	def __dispatch_keyboard_event(self, event):
		if 'Escape' == repr(event.keysym):
			self.__rootWidget.destroy()
		elif 'Up' == repr(event.keysym) or 'Down' == repr(event.keysym) or 'Right' == repr(event.keysym) or 'Left' == repr(event.keysym):
			self.get_player().set_direction(repr(event.keysym))
