background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'

import pygame
from pygame.locals import *
from sys import exit
import Vector2DClass

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

sprite_pos = Vector2DClass.Vec2d(200, 150)
sprite_speed = 300.

while True:
        for event in pygame.event.get():
                if event.type == QUIT:
                        exit()
                elif event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                                exit()
        
        pressed_keys = pygame.key.get_pressed()
        
        key_direction = Vector2DClass.Vec2d(0, 0)
        
        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
                key_direction[0] = -1
        elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
                key_direction[0] = 1
        if pressed_keys[K_UP] or pressed_keys[K_w]:
                key_direction[1] = -1
        elif pressed_keys[K_DOWN] or pressed_keys[K_s]:
                key_direction[1] = 1
                
        key_direction = key_direction.normalized()
        
        screen.blit(background, (0, 0))
        screen.blit(sprite, sprite_pos)
        
        time_passed = clock.tick(30)
        time_passed_seconds = time_passed / 1000.
        
        sprite_pos += key_direction * sprite_speed * time_passed_seconds
        
        pygame.display.update()
