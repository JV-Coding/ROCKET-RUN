## Class for the player rocket ##
import pygame


## Class for the player ##
rocket = pygame.image.load("Characters/space-ship.png")
damaged = pygame.image.load("Characters/player-damaged-1.png")
bullet = pygame.image.load("Characters/bullet.png")


class player(object):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height 
		self.speedx = 13
		self.speedy = 16
		self.hitbox = (self.x, self.y - 10, self.width - 50, self.height - 20)

	def draw_player(self, win):
		win.blit(rocket, (self.x, self.y))
		self.hitbox = (self.x, self.y, self.width, self.height)

	def move_up(self):
		self.y -= self.speedy
		if self.y < 60:
			self.y = 60

	def move_down(self):
		self.y += self.speedy
		if self.y > 790 - 128:
			self.y = 790 - 128

	def move_left(self):
		self.x -= self.speedx
		if self.x < 10:
			self.x = 10

	def move_right(self):
		self.x += self.speedx
		if self.x > 990:
			self.x = 990

	def player_damaged(self, win):
		self.hitbox = (self.x, self.y, self.width, self.height)
		win.blit(damaged, (self.x, self.y))


# Class for the player's bullets #
class Bullet(object):

	def __init__(self, x, y, width, height):
		
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.speed = 50

	def draw_bullet(self, window):
		window.blit(bullet, (self.x, self.y))
