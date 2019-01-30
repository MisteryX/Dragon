#! /usr/bin/python3
# -*- coding: utf8 -*-
__author__ = "Maxim Morskov"
__copyright__ = "Copyright 2019, Maxim Morskov"
__credits__ = ["Maxim Morskov"]
__maintainer__ = "Maxim Morskov"

from components.scene import Scene


class GameObject:

	__scene = None
	__X_cord = None
	__Y_cord = None
	__height = None
	__width = None
	__speed = None
	__direction = None

	def __init__(self, scene: Scene, X: int, Y: int):
		self.__scene = scene
		self.__X_cord = X
		self.__Y_cord = Y

	def get_position(self)->tuple:
		return self.__X_cord, self.__Y_cord

	def set_position(self, X: int, Y: int):
		self.__X_cord = X
		self.__Y_cord = Y

	def get_next_position(self)->tuple:
		X = self.__X_cord
		Y = self.__Y_cord
		if 'Right' == self.get_direction():
			X = X + self.get_speed()
		elif 'Left' == self.get_direction():
			X = Y - self.get_speed()
		elif 'Top' == self.get_direction():
			Y = Y - self.get_speed()
		elif 'Bottom' == self.get_direction():
			Y = Y + self.get_speed()
		return X, Y

	def get_direction(self):
		return self.__direction

	def set_direction(self, value: str):
		self.__direction = value

	def get_speed(self):
		return self.__speed

	def set_speed(self, value: int):
		self.__speed = value

	def get_height(self):
		return self.__height

	def get_width(self):
		return self.__width

	def get_scene(self):
		return self.__scene

	def draw(self, sprite_file_name: str):
		X, Y = self.get_position()
		self.get_scene().draw_sprite(X, Y, sprite_file_name)

	def move(self):
		pass
