background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'

import pygame
from pygame.locals import *
from sys import exit
from math import *
import Vector2DClass

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

#sprite_pos = Vector2DClass.Vec2d(200, 150)
sprite_pos = Vector2DClass.Vec2d(0, 0)
sprite_speed = 300.
sprite_rotation = 0.
sprite_rotation_speed = 360.
rw, rh = sprite.get_size()


while True:
        for event in pygame.event.get():
                if event.type == QUIT:
                        exit()
                elif event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                                exit()
        
        pressed_keys = pygame.key.get_pressed()
        
        rotation_direction = 0.
        movement_direction = 0.
        
        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
                rotation_direction = 1.
        elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
                rotation_direction = -1.
        if pressed_keys[K_UP] or pressed_keys[K_w]:
                movement_direction = -1.
        elif pressed_keys[K_DOWN] or pressed_keys[K_s]:
                movement_direction = 1.
        
        screen.blit(background, (0, 0))
        
        rotated_sprite = pygame.transform.rotate(sprite, sprite_rotation)
        
        w, h = rotated_sprite.get_size()
        sprite_draw_pos = Vector2DClass.Vec2d(sprite_pos[0] + rw/2 - w/2, sprite_pos[1] + rh/2 -h/2)
        
        screen.blit(rotated_sprite, sprite_draw_pos)
        
        time_passed = clock.tick(30)
        time_passed_seconds = time_passed / 1000.
        
        sprite_rotation += rotation_direction * sprite_rotation_speed * time_passed_seconds
        
        heading_x = sin(sprite_rotation*pi/180.)
        heading_y = cos(sprite_rotation*pi/180.)
        
        heading = Vector2DClass.Vec2d(heading_x, heading_y)
        
        heading *= movement_direction
        
        sprite_pos += heading * sprite_speed * time_passed_seconds
        
        pygame.display.update()