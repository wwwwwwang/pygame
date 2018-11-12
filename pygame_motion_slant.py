background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'

import pygame
from pygame.locals import *
from sys import *
from random import *

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

#x, y = 100., 100.
#speed_x, speed_y = 133., 170.
x, y = randint(0, 639), randint(0, 479)
speed_x, speed_y = randint(50, 100), randint(40, 80)

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				exit()
		
	screen.blit(background, (0, 0))
	screen.blit(sprite, (x, y))
	
	time_passed = clock.tick(30)
	time_passed_seconds = time_passed / 1000.
	
	#speed_x, speed_y = randint(50, 100), randint(40, 80)
	
	x += speed_x * time_passed_seconds
	y += speed_y * time_passed_seconds
	
	if x > 640 - sprite.get_width():
		speed_x = -speed_x
		x = 640 - sprite.get_width()
	elif x < 0:
		#speed_x = -speed_x
		speed_x = randint(50, 200)
		x = 0.
	
	if y > 480 - sprite.get_height():
		speed_y = -speed_y
		y = 480 - sprite.get_height()
	elif y < 0:
		#speed_y = -speed_y
		speed_y = randint(40, 150)
		y = 0.
		
	pygame.display.update()