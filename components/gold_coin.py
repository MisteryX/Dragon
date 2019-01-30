#! /usr/bin/python3
# -*- coding: utf8 -*-
__author__ = "Maxim Morskov"
__copyright__ = "Copyright 2019, Maxim Morskov"
__credits__ = ["Maxim Morskov"]
__maintainer__ = "Maxim Morskov"


from components.game_object import GameObject
from components.scene import Scene
import random


class GoldCoin(GameObject):
	SPRITE_FILE_NAME = 'resources/coin.png'
	POSITION_BUFFER = 30

	def __init__(self, scene: Scene, a_X=None, a_Y=None):
		if not a_X or not a_Y:
			a_X = random.randint(GoldCoin.POSITION_BUFFER, scene.get_option('width') - GoldCoin.POSITION_BUFFER)
			a_Y = random.randint(GoldCoin.POSITION_BUFFER, scene.get_option('height') - GoldCoin.POSITION_BUFFER)
		super().__init__(scene, a_X, a_Y)
