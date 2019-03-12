#! /usr/bin/python3
# -*- coding: utf8 -*-
__author__ = "Maxim Morskov"
__copyright__ = "Copyright 2019, Maxim Morskov"
__credits__ = ["Maxim Morskov"]
__maintainer__ = "Maxim Morskov"

from components.scene import Scene
from components.point import Point


class GameObject:

	__scene = None
	__position = None
	__previous_position = None
	__height = None
	__width = None
	__speed = None
	__direction = None
	__sprite = None

	def __init__(self, scene: Scene, position: Point):
		self.__scene = scene
		self.__X_cord = position.get_X()
		self.__Y_cord = position.get_Y()

	def get_sprite(self):
		return self.__sprite

	def get_position(self)->Point:
		return self.__position

	def get_position_xy(self)->tuple:
		return self.get_position().get_X(), self.get_position().get_Y()

	def set_position(self, value: Point):
		self.__previous_position = self.__position
		self.__position = value

	def set_position_xy(self, X: int, Y: int):
		self.get_position().set_X(X)
		self.get_position().set_Y(Y)

	def get_previous_position(self)->Point:
		return self.__previous_position

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
		X, Y = self.get_position_xy()
		self.get_scene().draw_sprite(X, Y, sprite_file_name)

	def move(self):
		X, Y = self.get_next_position()
		self.set_position_xy(X, Y)
