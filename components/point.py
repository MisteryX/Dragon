#! /usr/bin/python3
# -*- coding: utf8 -*-
__author__ = "Maxim Morskov"
__copyright__ = "Copyright 2019, Maxim Morskov"
__credits__ = ["Maxim Morskov"]
__maintainer__ = "Maxim Morskov"


class Point:
	__X = None
	__Y = None

	def __init__(self, X: int, Y: int):
		self.__X = X
		self.__Y = Y

	def get_X(self):
		return self.__X

	def set_X(self, value: int):
		self.__X = value

	def get_Y(self):
		return self.__Y

	def set_Y(self, value: int):
		self.__Y = value

