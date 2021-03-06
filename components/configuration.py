#! /usr/bin/python3
# -*- coding: utf8 -*-
__author__ = "Maxim Morskov"
__copyright__ = "Copyright 2019, Maxim Morskov"
__credits__ = ["Maxim Morskov"]
__maintainer__ = "Maxim Morskov"

from helpers.file_helper import FileHelper
import json


class Configuration:
	__options = None

	def __init__(self, **options):
		self.__options = self.get_stored_options(options.get('config_name', None))
		if not self.__options:
			self.__options = self.get_default_options()
		self.__options = {**self.__options, **options}

	def get_option(self, name):
		return self.__options.get(name, None)

	def set_option(self, name, value):
		self.__options[name] = value

	def get_options(self):
		return self.__options

	@staticmethod
	def get_stored_options(file_name: str)->dict:
		settings = FileHelper.get_text_file_content(file_name, True)
		if not settings:
			return {}
		options = {}
		try:
			options = json.loads(settings)
		except Exception as ex:
			pass
		return options

	@staticmethod
	def get_default_options()->dict:
		return {
			'field': {
				'height': 600,
				'width': 600,
				'bg': '000000',
				'bd': 0
			}
		}
