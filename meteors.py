# Class for the meteors #

import pygame
from random import randint

meteor = pygame.image.load('Characters/asteroid.png')

class Meteor(object):

	def __init__(self, width, height, velocity):

		self.x = randint(1250, 1500)
		self.y = randint(150, 600)
		self.width = width
		self.height = height
		self.velocity = velocity
		self.hitbox = (self.x + 10, self.y + 10, self.width-20, self.height-20)

	def draw_meteor(self, win):
		win.blit(meteor, (self.x, self.y))
		self.hitbox = (self.x + 10, self.y + 10, self.width-20, self.height-20)

	def destroyed(self, win):
		win.blit(meteor, (self.x, self.y))
		self.hitbox = (self.x + 10, self.y + 10, self.width-20, self.height-20)