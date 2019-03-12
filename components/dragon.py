#! /usr/bin/python3
# -*- coding: utf8 -*-
__author__ = "Maxim Morskov"
__copyright__ = "Copyright 2019, Maxim Morskov"
__credits__ = ["Maxim Morskov"]
__maintainer__ = "Maxim Morskov"

from components.game_object import GameObject
from components.scene import Scene


class Dragon(GameObject):
	HEAD_SPRITE_FILE_NAME = 'resources/dragon_head.png'
	HEAD_FOE_SPRITE_FILE_NAME = 'resources/foe_dragon_head.png'
	BODY_SPRITE_FILE_NAME = 'resources/dragon_body.png'

	__npc = None
	__tail = None
	__break_points = None

	def __init__(self, scene: Scene, npc: bool, **options):

		X = (scene.get_option('width') - self.__width) / 2
		Y = 0 if npc else (scene.get_option('height') - self.__height / 2)
		super().__init__(scene, X, Y)
		self.set_speed(options.get('speed', None))
		self.set_direction(options.get('direction', None))
		self.__npc = npc
		self.__tail = []
		self.__break_points = []
		self.draw(self.HEAD_SPRITE_FILE_NAME)

	def is_NPC(self):
		return self.__npc

	def set_direction(self, value: str):
		if self.get_direction() == value:
			return
		self.__direction = value
		self.__break_points.append(self.get_position())


