background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'

import pygame
from pygame.locals import *
#from sys import exit
import sys
sys.path.append('.')
#from 2DVectorClass import Vec2d
import Vector2DClass


pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

position = Vector2DClass.Vec2d(100., 100.)
heading = Vector2DClass.Vec2d(0, 0)

while True:
	for event in pygame.event.get():
		if event.type ==QUIT:
			print("found clicking 'X', and exit...")
			exit()
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				print("found pressing down esc, and exit...")
				exit()
	
	screen.blit(background, (0, 0))
	screen.blit(sprite, position)
	
	time_passed = clock.tick(30)
	time_passed_seconds = time_passed / 1000.
	
	destination = Vector2DClass.Vec2d( *pygame.mouse.get_pos() ) - Vector2DClass.Vec2d( *sprite.get_size() )/2
	vector_to_mouse = Vector2DClass.Vec2d.__sub__(destination, position)
	#vector_to_mouse = vector_to_mouse.normalized()
	
	heading = heading*0.97 +  vector_to_mouse * .6
	
	position = position.__add__(heading * time_passed_seconds)
	
	#print("time_passed_seconds=",time_passed_seconds,", vector_to_mouse=",str(vector_to_mouse),", heading=",str(heading),", position=",str(position))
	
	pygame.display.update()
	



