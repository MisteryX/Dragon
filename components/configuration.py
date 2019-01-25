#! /usr/bin/python3
# -*- coding: utf8 -*-
__author__ = "Maxim Morskov"
__copyright__ = "Copyright 2019, Maxim Morskov"
__credits__ = ["Maxim Morskov"]
__maintainer__ = "Maxim Morskov"


class Configuration:
	__options = None

	def __init__(self, **options):
		pass

	def get_option(self, name):
		return self.__options.get(name, None)

	def set_option(self, name, value):
		self.__options[name] = value

	def get_options(self):
		return self.__options

