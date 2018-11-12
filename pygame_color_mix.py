#!/usr/bin/env python

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

color1 = (221, 99, 20)
color2 = (96, 130, 51)
factor = 0.

def blend_color(color1, color2, blend_factor):
	r1, g1, b1 = color1
	r2, g2, b2 = color2
	r = r1 + (r2 - r1) * blend_factor
	g = g1 + (g2 - g1) * blend_factor
	b = b1 + (b2 - b1) * blend_factor
	return int(r), int(g), int(b)

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
	
	screen.fill((255, 255, 255))
	
	tri = [(10, 120), (629, 60), (629, 180)]
	pygame.draw.polygon(screen, (0, 127, 10), tri)
	pygame.draw.circle(screen, (127,0,0), (int(factor * 639.), 120), 10)
	
	x, y = pygame.mouse.get_pos()
	if pygame.mouse.get_pressed()[0]:
		factor = x / 639.
		pygame.display.set_caption("PyGame Color Blend Test - %.3f" % factor)
	
	color = blend_color(color1, color2, factor)
	
	pygame.draw.rect(screen, color, (40, 250, 560, 220))
	
	pygame.display.update()