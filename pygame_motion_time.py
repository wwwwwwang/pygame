background_image_file = 'sushiplate.jpg'
sprite_image_file = 'fugu.png'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_file).convert()
sprite = pygame.image.load(sprite_image_file)

clock = pygame.time.Clock()

x = 0.

speed = 250

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
			
	screen.blit(background, (0, 0))
	screen.blit(sprite, (x, 100))
	
	time_passed = clock.tick()
	print("time_passed = %d"%time_passed)
	time_passed_second = time_passed /1000.0
	
	distance_moved = time_passed_second * speed
	
	x += distance_moved
	
	if x > 640.:
		x -= 640.
		#x = 0.
	
	pygame.display.update()
