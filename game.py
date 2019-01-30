#! /usr/bin/python3
# -*- coding: utf8 -*-
__author__ = "Maxim Morskov"
__copyright__ = "Copyright 2019, Maxim Morskov"
__credits__ = ["Maxim Morskov"]
__maintainer__ = "Maxim Morskov"

import sys
import argparse
from components.configuration import Configuration
from components.scene import Scene
from components.dragon import Dragon
from components.gold_coin import GoldCoin


class Game:
	__options = None
	__scene = None
	__objects = None

	def __init__(self, **options):
		self.__options = Configuration(options)
		self.__scene = Scene(self.get_option('scene'))
		self.__init_objects()

	def __init_objects(self):
		self.__objects = []
		self.__objects.append(Dragon(self.get_scene(), self.get_option('player')), True)
		self.__objects.append(GoldCoin(self.get_scene()))

	def get_option(self, name: str):
		return self.__options.get(name, None)

	def get_scene(self)->Scene:
		return self.__scene

	def run(self):
		result = True
		while result:
			result = self.get_scene().update()


def get_params_using_parser(args: list):
	params_parser = argparse.ArgumentParser()

	params_parser.add_argument(
		'-c', '--config_file',
		type=str, help='path to config file',
		default='settings.json'
	)
	return params_parser.parse_args(args)


def main(a_params):
	game = Game(**a_params)
	game.run()


# --== Entry point ==--
if __name__ == "__main__":
	script_params = get_params_using_parser(sys.argv[1:])
	main(script_params)

