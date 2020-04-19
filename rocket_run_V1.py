##### Rocket Run Game (Version 1) #####


import pygame
import os
import time
from random import randint

# importing all the self made modules #
from rocketplayer import player
from rocketplayer import Bullet
from meteors import Meteor
from enemy import Enemy
from enemy import Bullet_enemy
from Missile import Enemy_missile
import button_function


#######################################################################################
#######################################################################################

clock = pygame.time.Clock()
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()


#DISPLAY SETTINGS
pygame.display.set_caption('ROCKET RUN')
window_width = 1200
window_height = 800
window_display = pygame.display.set_mode((window_width, window_height))


# Defining some colours #

grey = (150, 150, 150)
number_colour = (255, 255, 255)


# Images #

rocket = pygame.image.load('Characters/space-ship.png')


# Player points at the start of the game#
points = 0


######################################################################################
######################################################################################

# Intro of the game #
def game_intro():

	time.sleep(0.5)

	def draw_to_window():
		# Drawing the background #
		window_display.blit(bg1, (bg_x, bg_y))
		window_display.blit(bg2, (bg_x2, bg_y2))
		window_display.blit(bg3, (bg_x3, bg_y3))

		# Drawing the intro title #
		window_display.blit(intro_title, (165, 100))

		# Drawing the highscore #
		window_display.blit(high_score_label, (440, 240))

		# Play button #
		play_btn = button_function.button(window_display, "Play Rocket Run!", 385, 350, 400, 100, (100, 100, 100), (250, 250, 250), instructions)
	



	# Background Images + motion #
	bg1 = pygame.image.load('background Images/bg1.png').convert()
	bg2 = pygame.image.load('background Images/bg2.png').convert()
	bg3 = pygame.image.load('background Images/bg3.png').convert()
	bg_x = 0
	bg_y = 0
	bg_x2 = bg2.get_width()
	bg_y2 = 0
	bg_x3 = bg1.get_width() + bg2.get_width()
	bg_y3 = 0
	bg_vel = 5

	# Intro title #
	title_font = pygame.font.SysFont("comicsans", 180, True)
	intro_title = title_font.render("Rocket Run", 1, (255, 255, 255))


	# High score #
	font = pygame.font.SysFont("comicsans", 50, True) 
	try:
		highscore_file = open("highscore.txt", "r")
		highscore = highscore_file.read()
		if len(highscore) <= 0:
			highscore = 0
		else:
			existing_highscore = highscore
			highscore_file.close()
	except:
		highscore_file = open("highscore.txt", "w+")
		highscore_file.close()


	high_score_label = font.render("Highscore: " + str(highscore), 1, (255, 255, 255))


	# background music
	pygame.mixer.music.load('Sound effects/Milos.mp3')
	pygame.mixer.music.play(-1)

	# Total points #




	intro = True
	while intro:

		draw_to_window()

		# Move the background Images #
		bg_x -= bg_vel
		bg_x2 -= bg_vel
		bg_x3 -= bg_vel

		# Moving the background Images
		if bg_x < bg1.get_width()*-1:
			bg_x = bg1.get_width() + bg2.get_width()
			bg_x -= bg_vel
		if bg_x2 < bg2.get_width()*-1:
			bg_x2 = bg2.get_width() + bg2.get_width()
			bg_x2 -= bg_vel
		if bg_x3 < bg3.get_width()*-1:
			bg_x3 = bg3.get_width() + bg3.get_width()
			bg_x3 -= bg_vel

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		# FPS
		clock.tick(30)


		pygame.display.update()




#######################################################################################
#######################################################################################

# Pausing function during the gameplay #
pause = False

def unpause_game():
	global pause
	pygame.mixer.music.unpause()
	pause = False


def paused():
	global pause
	pause = True
	# music stops
	pygame.mixer.music.pause()

	# Paused Text #
	font = pygame.font.SysFont("comicsans", 80, True)
	pause_text = font.render("Rocket Run Paused", 1, (255, 255, 255))

	# FPS
	clock.tick(30)


	# Drawing to the window #
	def draw_to_window():
		# title #
		window_display.blit(pause_text, (265, 100))

		# Pause Buttons #
		unpause_btn = button_function.button(window_display, "Continue Rocket Run!", 385, 200, 400, 100, (100, 100, 100), (250, 250, 250), unpause_game)
		restart_btn = button_function.button(window_display, "Restart Game", 385, 350, 400, 100, (100, 100, 100), (250, 250, 250), main_loop)
		quit_btn = button_function.button(window_display, "Quit Game", 385, 500, 400, 100, (100, 100, 100), (250, 250, 250),game_intro)
		

	# Event handling
	while pause:

		draw_to_window()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		pygame.display.update()






########################################################################################
########################################################################################

# Ending the game if the health reaches 0
end = False

def ending_game():
	global points

	new_highscore = None

	global end
	end = True
	global quit_game
	quit_game = True

	# music stops
	pygame.mixer.music.pause()
	Explosion = pygame.mixer.Sound('Sound effects/Ending_explosion.wav')
	Explosion.play(0)

	# You lost title #
	title_count = 0
	font = pygame.font.SysFont("comicsans", 80, True)
	score_font = pygame.font.SysFont("comicsans", 50, True) 
	end_text = font.render("Oh no! You got destroyed! ", 1, (255, 255, 255))
	score = score_font.render("You scored: " + str(points), 1, (255, 255, 255))

	# saving the score to the highscore file, if it is higher #
	highscore_file = open("highscore.txt", "r")
	existing_highscore = highscore_file.read()
	
	if len(existing_highscore) <= 0:
		if int(points) > 0:
			highscore_file = open("highscore.txt", "w")
			highscore_file.write(str(points))
			highscore_file.close()
			new_highscore = points
	
	if len(existing_highscore) != 0:
		if int(points) > int(existing_highscore):
			highscore_file = open("highscore.txt", "w")
			highscore_file.write(str(points))
			highscore_file.close()
			new_highscore = points

	# draw to window #
	def draw_to_window():
		window_display.blit(score, (430, 165))

		# End of game buttons #
		play_again_btn = button_function.button(window_display, "Play again", 100, 550, 400, 100, (100, 100, 100), (250, 250, 250), main_loop)
		quit_btn = button_function.button(window_display, "Return to Menu", 680, 550, 400, 100, (100, 100, 100), (250, 250, 250), game_intro)
	

	while end:

		title_count += 1

		draw_to_window()

		if new_highscore != None:
			high_font = pygame.font.SysFont("comicsans", 65, True, True)
			high_label = high_font.render("Well done! You beat your highscore!", 1, (255, 255, 255))
			window_display.blit(high_label, (170, 300))

		if title_count > 200:
			title_count += 1
			window_display.blit(end_text, (200, 70))
		if title_count <= 200:
			title_count += 1
		if title_count > 900:
			title_count = 0

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()


		pygame.display.update()



#########################################################################################
#########################################################################################

# Instructions for the game #
def instructions():

	time.sleep(0.5)

	def draw_to_window():
		# Drawing the background #
		window_display.blit(bg1, (bg_x, bg_y))
		window_display.blit(bg2, (bg_x2, bg_y2))
		window_display.blit(bg3, (bg_x3, bg_y3))

		# title #
		window_display.blit(title, (350, 80))

		# Instrcutions #
		window_display.blit(instrcutions_section, (40, 210))
		window_display.blit(instrcutions_section2, (40, 265))
		window_display.blit(instrcutions_section3, (40, 320))

		# Play button #
		play_btn = button_function.button(window_display, "Let's play!", 890, 700, 250, 70, (100, 100, 100), (250, 250, 250), main_loop)
	



	# Background Images + motion #
	bg1 = pygame.image.load('background Images/bg1.png').convert()
	bg2 = pygame.image.load('background Images/bg2.png').convert()
	bg3 = pygame.image.load('background Images/bg3.png').convert()
	bg_x = 0
	bg_y = 0
	bg_x2 = bg2.get_width()
	bg_y2 = 0
	bg_x3 = bg1.get_width() + bg2.get_width()
	bg_y3 = 0
	bg_vel = 5


	# background music
	pygame.mixer.music.load('Sound effects/Milos.mp3')
	pygame.mixer.music.play(-1)

	# title #
	title_font = pygame.font.SysFont("comicsans", 100, True)
	title = title_font.render("How to play...", 1, (255, 255, 255))

	# Instructions #
	font = pygame.font.SysFont("comicsans", 50, True)
	instrcutions_section = font.render("Use the 'w' key to move up, 's' key to move down,", 1, (255, 255, 255))
	instrcutions_section2 = font.render("'a' key to move left and the 'd' key to move right.", 1, (255, 255, 255))
	instrcutions_section3 = font.render("Press SPACE to shoot the bullets", 1, (255, 255, 255))




	instructions_part = True
	while instructions_part:

		draw_to_window()

		# Move the background Images #
		bg_x -= bg_vel
		bg_x2 -= bg_vel
		bg_x3 -= bg_vel

		# Moving the background Images
		if bg_x < bg1.get_width()*-1:
			bg_x = bg1.get_width() + bg2.get_width()
			bg_x -= bg_vel
		if bg_x2 < bg2.get_width()*-1:
			bg_x2 = bg2.get_width() + bg2.get_width()
			bg_x2 -= bg_vel
		if bg_x3 < bg3.get_width()*-1:
			bg_x3 = bg3.get_width() + bg3.get_width()
			bg_x3 -= bg_vel

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		# FPS
		clock.tick(30)


		pygame.display.update()




#########################################################################################
#########################################################################################


## Main Game Loop Function ##
def main_loop():

	global points
	points = 0


	# background music
	pygame.mixer.music.load('Sound effects/Milos.mp3')
	pygame.mixer.music.play(-1)  

	# sound effects #
	enemy_shot = pygame.mixer.Sound('Sound effects/enemy_shot.wav')            



	# Drawing the images to the window surface #
	def draw_to_window():
		# Drawing the background #
		window_display.blit(bg1, (bg_x, bg_y))
		window_display.blit(bg2, (bg_x2, bg_y2))
		window_display.blit(bg3, (bg_x3, bg_y3)) 
		
		# Drawing the score #
		pygame.draw.rect(window_display, (23, 10, 70), (0, 0, window_width, 50))
		score = font.render("Score: " + str(points), 1, (255, 255, 255))
		window_display.blit(score, (10, 10))

		# Drawing the health #
		health_bar = font.render("Health:", 1, (255, 255, 255))
		window_display.blit(health_bar, (250, 10))

		# Drawing the health bar #
		red = pygame.draw.rect(window_display, (255, 0, 0), (400, 10, red_w, 33))
		green = pygame.draw.rect(window_display, (0, 200, 0), (400, 10, green_w, 33))
		health_number_text = font.render(str(health_number) + " / " + str(total_player_health), 1, number_colour)
		window_display.blit(health_number_text, (410, 10))

		# Drawing the player's bullet #
		for bullet in bullets_shot:
			bullet.draw_bullet(window_display)
		
		# Drawing the player #
		player_rocket.draw_player(window_display)

		# Drawing the meteors
		for meteor in meteor_list:
			meteor.draw_meteor(window_display)

		# Drawing the enemy bullets #
		for enemy_bullet in enemy_bullet_list:
			enemy_bullet.draw_enemy_bullet(window_display)

		# Drawing the missiles #
		for missile in missiles:
			missile.draw_missile(window_display)





	# POINTS #
	font = pygame.font.SysFont("comicsans", 50, True)


	# Health of the player  + health bar coordinates #
	total_player_health = 100
	health_number = 100
	green_w = total_player_health * 2
	red_w = green_w


	# Calling the player class from module #
	player_x = 100
	player_y = window_height/2-128/2
	player_width = 128
	player_height = 128
	player_rocket = player(player_x, player_y, player_width, player_height)
	player_y_speed = 16
	player_x_speed = 13

	# bullet list (player) #
	bullets_shot = []
	shootloop = 0



	# Enemy Class #
	enemy_x = randint(3000, 3200)
	enemy_y = randint(100, 300)
	enemy_end = randint(450, 600)
	enemy_UFO = Enemy(enemy_x, enemy_y, 128, 128, 7, enemy_end)
	enemy_count = 0


	# bullet list (enemy) #
	enemy_bullet_list = []
	loop = 1


	# missile list #
	missiles = []
	missile_count = 0


	# Meteor list #
	meteor_list = []
	number_meteors = randint(1, 3)
	meteor_speed = randint(10, 20)


	# Background Images + motion #
	bg1 = pygame.image.load('background Images/bg1.png').convert()
	bg2 = pygame.image.load('background Images/bg2.png').convert()
	bg3 = pygame.image.load('background Images/bg3.png').convert()
	bg_x = 0
	bg_y = 0
	bg_x2 = bg2.get_width()
	bg_y2 = 0
	bg_x3 = bg1.get_width() + bg2.get_width()
	bg_y3 = 0
	bg_vel = 7


	quit_game = False
	while not quit_game:

		# creating a loop for the shooting function #
		if shootloop > 0:
			shootloop += 1
		if shootloop > 3:
			shootloop = 0


		# Move the background Images #
		bg_x -= bg_vel
		bg_x2 -= bg_vel
		bg_x3 -= bg_vel


		# Moving the background Images back to original position when they reach the end #
		if bg_x < bg1.get_width()*-1:
			bg_x = bg1.get_width() + bg2.get_width()
			bg_x -= bg_vel
		if bg_x2 < bg2.get_width()*-1:
			bg_x2 = bg2.get_width() + bg2.get_width()
			bg_x2 -= bg_vel
		if bg_x3 < bg3.get_width()*-1:
			bg_x3 = bg3.get_width() + bg3.get_width()
			bg_x3 -= bg_vel


		# Drawing the background and other images #
		draw_to_window()

		enemy_UFO.draw_enemy(window_display)
		enemy_UFO.enemy_movement()



		# Events #
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit_game = True
				pygame.quit()
				quit()


		
		# for loop for the bullets + collision between the bullet and the meteor #
		for bullet in bullets_shot:
			for meteor in meteor_list:
				if bullet.y < meteor.hitbox[1] + meteor.hitbox[3] and bullet.y + bullet.height > meteor.hitbox[1]:
					if bullet.x + bullet.width > meteor.hitbox[0] and bullet.x - bullet.width < meteor.hitbox[0]+ meteor.hitbox[2]:
						try:
							meteor_list.pop(meteor_list.index(meteor))
							bullets_shot.pop(bullets_shot.index(bullet))
							points += 50
						except:
							IOError
					else:
						pass
				else:
					pass 

		# finding collision between the bullet and enemy #
		for bullet in bullets_shot:
			if bullet.y < enemy_UFO.hitbox[1] + enemy_UFO.hitbox[3] and bullet.y + bullet.height > enemy_UFO.hitbox[1]:
				if bullet.x + bullet.width > enemy_UFO.hitbox[0] and bullet.x - bullet.width < enemy_UFO.hitbox[0]+ enemy_UFO.hitbox[2]:
					try:
						bullets_shot.pop(bullets_shot.index(bullet))
						enemy_bullet_list.pop(enemy_bullet_list.index(enemy_bullet))
						enemy_x = randint(1500, 1800)
						enemy_y = randint(100, 250)
						enemy_end = randint(450, 600)
						enemy_UFO = Enemy(enemy_x, enemy_y, 128, 128, 7, enemy_end)
						enemy_UFO.draw_enemy(window_display)
						enemy_UFO.enemy_movement()
						if len(enemy_bullet_list ) < 1:
							speed = 20
							enemy_bullet_list.append(Bullet_enemy(round(enemy_UFO.hitbox[0]), round(enemy_UFO.hitbox[1] + 50), 32, 32, speed))
						points += 100
					except:
						IOError



			# Moving the player bullet if its on the screen #
			if bullet.x < 1200 and bullet.x > 0:
				bullet.x += bullet.speed
			else:
				try:
					bullets_shot.pop(bullets_shot.index(bullet))
				except:
					IOError 


			# moving the enemy bullet #
		for enemy_bullet in enemy_bullet_list:

			if enemy_bullet.x < 1200 and enemy_bullet.x > 0:
				enemy_bullet.x -= enemy_bullet.speed
			else:
				try:
					enemy_bullet_list.pop(enemy_bullet_list.index(enemy_bullet))
				except:
					IOError

			if enemy_bullet.x < 1200 and enemy_bullet.x > 970:
				if len(enemy_bullet_list) == 1:
					enemy_shot.play()

		if len(enemy_bullet_list ) < 1:
			speed = 20
			enemy_bullet_list.append(Bullet_enemy(round(enemy_UFO.hitbox[0]), round(enemy_UFO.hitbox[1] + 50), 32, 32, speed))



		# checking for collisions between the enemy bullet and player rocket #
		for enemy_bullet in enemy_bullet_list:
			if enemy_bullet.y < player_rocket.hitbox[1] + player_rocket.hitbox[3] and enemy_bullet.y + enemy_bullet.height > player_rocket.hitbox[1]:
				if enemy_bullet.x + enemy_bullet.width > player_rocket.hitbox[0] and enemy_bullet.x - enemy_bullet.width < player_rocket.hitbox[0]+ player_rocket.hitbox[2]:
					
					player_rocket.player_damaged(window_display)
	
					try:
						enemy_bullet_list.pop(enemy_bullet_list.index(enemy_bullet))
						green_w -= (round(total_player_health * 2 / (total_player_health  / 10)))
						health_number -= 10
					except:
						IOError			



		# Finding the collision between the rocket and meteors #
		for meteor in meteor_list:
			if meteor.hitbox[1] < player_rocket.hitbox[1] + player_rocket.hitbox[3] and meteor.hitbox[1] + meteor.hitbox[3] > player_rocket.hitbox[1]:
				if meteor.hitbox[0] + meteor.hitbox[2] > player_rocket.hitbox[0] and meteor.hitbox[0] < player_rocket.hitbox[0] + player_rocket.hitbox[2]:
					
					player_rocket.player_damaged(window_display)

					try:
						meteor_list.pop(meteor_list.index(meteor))
						green_w -= (round(total_player_health * 2 / (total_player_health  / 5))) 
						health_number -= 5
					except:
						IOError
				else:
					pass
			else:
				pass


		# moving the meteors if they fit the criteria, otherwise delete them #
		for meteor in meteor_list:
			if meteor.x < 1400 and meteor.x > -128:
				meteor.x -= meteor.velocity
			else:
				try:
					meteor_list.pop(meteor_list.index(meteor))
					number_meteors = randint(1, 5)
					meteor_speed = randint(10, 20)
				except:
					IOError


		if len(meteor_list) < number_meteors:
			meteor_list.append(Meteor(128, 128, meteor_speed)) 



		# missile movements + collision between the missile and player and also collsion between player bullet and missile #
		for missile in missiles:
			if missile.x < 13500 and missile.x > -128:
				missile.x -= missile.speed
				if missile.x < 1900 and missile.x > 1200:
					warning_mark_font = pygame.font.SysFont("comicsans", 250, True)
					warning_mark = warning_mark_font.render("!", 1, (255, 0, 0))
					window_display.blit(warning_mark, (1100, missile.y)) 
			else:
				try:
					missiles.pop(missiles.index(missile))
				except:
					IOError

			if missile.hitbox[1] < player_rocket.hitbox[1] + player_rocket.hitbox[3] and missile.hitbox[1] + missile.hitbox[3] > player_rocket.hitbox[1]:
				if missile.hitbox[0] + missile.hitbox[2] > player_rocket.hitbox[0] and missile.hitbox[0] < player_rocket.hitbox[0] + player_rocket.hitbox[2]:
					
					player_rocket.player_damaged(window_display)

					try:
						missiles.pop(missiles.index(missile))
						health_number -= 20
						green_w -= (round(total_player_health * 2 / (total_player_health  / 20)))
					except:
						IOError 

			for bullet in bullets_shot:
				if bullet.y < missile.hitbox[1] + missile.hitbox[3] and bullet.y + bullet.height > missile.hitbox[1]:
					if bullet.x + bullet.width > missile.hitbox[0] and bullet.x - bullet.width < missile.hitbox[0]+ missile.hitbox[2]:
						try:
							missiles.pop(missiles.index(missile))
							bullets_shot.pop(bullets_shot.index(bullet))
							points += 500
						except:
							IOError
					 

					 
		# Creating the missiles #
		number_of_missiles_1 = 1
		number_of_missiles_2 = 2
		if len(missiles) < number_of_missiles_1 and missile_count < 3:
			missile_x = randint(12000, 13000)
			missile_y = randint(70, 600)
			missiles.append(Enemy_missile(missile_x, missile_y, 128, 128, 45))
			missile_count += 1

		if len(missiles) < number_of_missiles_2 and missile_count >= 3:
			missile_x = randint(5000, 6000)
			missile_y = randint(70, 600)
			missiles.append(Enemy_missile(missile_x, missile_y, 128, 128, 45))
			missile_count += 1


		# Rocket movements #
		try:
			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_w:
					player_rocket.move_up()
					
				elif event.key == pygame.K_s:
					player_rocket.move_down()
					

				elif event.key == pygame.K_a:
					player_rocket.move_left()
					

				elif event.key == pygame.K_d:
					player_rocket.move_right()
					


				# Shooting the bullets #
				if event.key == pygame.K_SPACE:
					if len(bullets_shot) < 1:
						bullets_shot.append(Bullet(round(player_rocket.hitbox[0] + 100), round(player_rocket.hitbox[1] + 51), 24, 24))
						shootloop = 1
		except:
			IOError


		# Ending the game if health reaches 0 #
		if health_number <= 0:
			green_w = 0
			health_number = 0
			ending_game()
			end = True
			quit_game = True
			
		# FPS
		clock.tick(30)


		# pause button #
		pause_btn = button_function.button(window_display, "||", 1150, 5, 40, 40, (150, 0, 0), (250, 0, 0), paused)



		# warnings for the player about their health #
		if health_number < 30 and health_number >= 20:
			if loop > 0:
				loop += 1
			if loop > 10:
				loop += 1
				health_bar = font.render("low health!", 1, (255, 255, 255))
				window_display.blit(health_bar, (650, 10))
			if loop > 20:
				loop = 1

		if health_number < 20:
			if loop > 0:
				loop += 1
			if loop > 10:
				loop += 1
				health_bar = font.render("critical health!", 1, (255, 255, 255))
				window_display.blit(health_bar, (650, 10))
			if loop > 20:
				loop = 1


		pygame.display.update()

	pygame.quit()




## calling the functions for starting page ##
game_intro()



