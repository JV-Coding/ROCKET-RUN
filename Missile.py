import pygame
from random import randint


missile = pygame.image.load('Characters/missile.png')
class Enemy_missile(object):

	def __init__(self, x, y, width, height, speed):

		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.speed = speed
		self.hitbox = (self.x, self.y + 30, self.width, self.height - 60)

	def draw_missile(self, window):
		self.hitbox = (self.x, self.y + 30, self.width, self.height - 60)
		window.blit(missile, (self.x, self.y))