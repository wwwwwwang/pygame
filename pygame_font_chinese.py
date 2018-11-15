# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

#font = pygame.font.SysFont("arial", 40)
font = pygame.font.SysFont("方正兰亭超细黑简体", 40)

text_surface = font.render(u"你好", True, (0, 0, 255))

x = 0
y = (480 -text_surface.get_height())/2

background = pygame.image.load("sushiplate.jpg").convert()

while True:
        for event in pygame.event.get():
                if event.type == QUIT:
                        exit()
                
                screen.blit(background, (0,0))
                
                x -= 2
                if x < -text_surface.get_width():
                        x = 640 - text_surface.get_width()
                
                screen.blit(text_surface, (x, y))
                
                pygame.display.update()