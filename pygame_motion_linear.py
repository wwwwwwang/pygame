background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'

import pygame
from pygame.locals import *
from sys import exit
from random import *

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)

#x = randint(0, 639)
#y = randint(0, 479)
x = 0.

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
	
	screen.blit(background, (0, 0))
	screen.blit(sprite, (x, 100))
	
	#x += randint(-3, 3)
	#y += randint(-2, 2)
	
	#if x > 640:
	#	x -= 640
	#if x < 0:
	#    x += 640
	#if y > 480:
	#	y -= 480
	#if y < 0:
	#	y += 480
	
	x += .5
	
	if x > 640.:
		x = 0.
		
	pygame.display.update()