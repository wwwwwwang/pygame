SCREEN_SIZE = (640, 480)

GRAVITY = 250.
BOUNCINESS = .73

import pygame
from pygame.locals import *
from random import randint
from Vector2DClass import Vec2d

def stero_pan(x_coord, screen_width):
	right_volume = float(x_coord)/screen_width
	left_volume = 1.0 - right_volume
	return (left_volume, right_volume)
	
class Ball(object):
	def __init__(self, position, speed, image, bounce_sound):
		self.position = Vec2d(position)
		self.speed = Vec2d(speed)
		self.image = image
		self.bounce_sound = bounce_sound
		self.age = 0.0
		
	def update(self, time_passed):
		w, h = self.image.get_size()
		screen_width, screen_height = SCREEN_SIZE
		
		x, y = self.position
		x -= w/2
		y -= h/2
		
		bounce = False
		
		if y+h > screen_height:
			self.speed[1] = -self.speed[1] * BOUNCINESS
			self.position[1] = screen_height - h/2. - 1.
			bounce = True
			
		if x <= 0:
			self.speed[0] = -self.speed[0] * BOUNCINESS
			self.position[0] = w/2. + 1.
		
		if x+w > screen_width:
			self.speed[0] = -self.speed[0] * BOUNCINESS
			self.position[0] = screen_width - w/2. - 1.
			bounce = True
			
		
		self.position += self.speed * time_passed
		self.speed[1] += time_passed * GRAVITY
		
		if bounce:
			self.play_bounce_sound()
			
		self.age += time_passed
		
	def play_bounce_sound(self):
		channel = self.bounce_sound.play()
		
		if channel is not None:
			left, right = stero_pan(self.position[0], SCREEN_SIZE[0])
			channel.set_volume(left, right)
			
	def render(self, surface):
		w, h = self.image.get_size()
		x, y = self.position
		x -= w/2
		y -= h/2
		surface.blit(self.image, (x, y))
		
def run():
	pygame.mixer.pre_init(44100, 16, 2, 1024*4)
	pygame.init()
	pygame.mixer.set_num_channels(8)
	
	screen = pygame.display.set_mode(SCREEN_SIZE, 0)
	
	pygame.mouse.set_visible(False)
	
	clock = pygame.time.Clock()
	
	ball_image = pygame.image.load("ball.png").convert_alpha()
	mouse_image = pygame.image.load("mousecursor.png").convert_alpha()
	
	bounce_sound = pygame.mixer.Sound("bounce.ogg")
	balls = []
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
			if event.type == MOUSEBUTTONDOWN:
				random_speed = ( randint(-400, 400), randint(-300, 0) )
				new_ball = Ball( event.pos, random_speed, ball_image, bounce_sound )
				balls.append(new_ball)
				
		time_passed_seconds = clock.tick() / 1000.
		screen.fill((255, 255, 255))
		
		deal_balls = []
		
		for ball in balls:
			ball.update(time_passed_seconds)
			ball.render(screen)
			
			if ball.age > 25.0:
				deal_balls.append(ball)
				
		for ball in deal_balls:
			balls.remove(ball)
			
		mouse_pos = pygame.mouse.get_pos()
		screen.blit(mouse_image, mouse_pos)
		pygame.display.update()
		
if __name__ == "__main__":
	run()