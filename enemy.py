# This is the enemy file #

import pygame
from random import randint

enemy_ufo = pygame.image.load('Characters/enemy-ufo.png')
enemy_bullet = pygame.image.load('Characters/enemy bullet.png')

class Enemy(object):

	def __init__(self, x, y, width, height, speed, end):

		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.speed = speed
		self.hitbox = (self.x + 15, self.y + 15, self.width - 30, self.height - 30)
		self.path = [y, end]

	def draw_enemy(self, win):
		win.blit(enemy_ufo, (self.x, self.y))
		self.hitbox = (self.x + 15, self.y + 15, self.width - 30, self.height - 30)

	def enemy_movement(self):

		# moving to the screen #
		if self.speed > 0 and self.x > 1000:
			self.x -= self.speed
			self.y += 0

		else:
			self.x += 0

			# moving down
			if self.speed > 0:
				if self.y < self.path[1] + self.speed:
					self.y += self.speed
				else:
					self.speed = self.speed * -1
					self.y += self.speed
			# moving up
			else:
				if self.y > self.path[0] - self.speed:
					self.y += self.speed
				else:
					self.speed = self.speed * -1
					self.y += self.speed
			


class Bullet_enemy(object):

	def __init__(self, x, y, width, height, speed):
		
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.speed = speed

	def draw_enemy_bullet(self, window):
		window.blit(enemy_bullet, (self.x, self.y))



	
				

