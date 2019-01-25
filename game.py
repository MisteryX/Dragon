#! /usr/bin/python3
# -*- coding: utf8 -*-
__author__ = "Maxim Morskov"
__copyright__ = "Copyright 2019, Maxim Morskov"
__credits__ = ["Maxim Morskov"]
__maintainer__ = "Maxim Morskov"

import sys
import argparse


class Game:
	__params = None
	__field = None
	__dragon = None

	def __init__(self, **options):
		self.__params = options

	def run(self):
		pass


def get_params_using_parser(args: list):
	params_parser = argparse.ArgumentParser()

	params_parser.add_argument(
		'-c', '--config_file',
		type=str, help='path to config file',
		default='configs/brain_config.json'
	)
	params_parser.add_argument(
		'-s', '--server',
		type=str, help='server to get config',
		default=''
	)
	return params_parser.parse_args(args)


def main(params):
	game = Game(**params)
	game.run()


# --== Entry point ==--
if __name__ == "__main__":
	params = get_params_using_parser(sys.argv[1:])
	main(params)

