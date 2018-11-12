import pygame
from pygame.locals import *
from Vector3DClass import Vec3d

from math import *
from random import randint

SCREEN_SIZE = (640, 480)
CUBE_SIZE = 300

def calculate_viewing_distance(fov, screen_with):
	d = (screen_with/2.) / tan(fov/2.)
	return d
	
def run():
	pygame.init()
	screen = pygame.display.set_mode(SCREEN_SIZE, 0)
	
	default_font = pygame.font.get_default_font()
	font = pygame.font.SysFont(default_font, 24)
	
	ball = pygame.image.load("basketball.png").convert_alpha()
	
	points = []
	
	fov = 90.
	viewing_distance = calculate_viewing_distance(radians(fov), SCREEN_SIZE[0])
	
	for x in range(0, CUBE_SIZE+1, 20):
		edge_x = x == 0 or x == CUBE_SIZE
		
		for y in range(0, CUBE_SIZE+1, 20):
			edge_y = y == 0 or y == CUBE_SIZE
				
			for z in range(0, CUBE_SIZE+1, 20):
				edge_z = z == 0 or z == CUBE_SIZE
				
				if sum((edge_x, edge_y, edge_z)) >= 2:
					point_x = float(x) - CUBE_SIZE/2
					point_y = float(y) - CUBE_SIZE/2
					point_z = float(z) - CUBE_SIZE/2
					
					points.append(Vec3d(point_x, point_y, point_z))
					
	def get_point_z(point):
		return point[2]
	
	points.sort(key=get_point_z, reverse=False)
	
	center_x, center_y = SCREEN_SIZE
	center_x /= 2
	center_y /= 2
	ball_center_x, ball_center_y = ball.get_size()
	ball_center_x /= 2
	ball_center_y /= 2
	
	camera_position = Vec3d(0.0, 0.0, 700.)
	camera_speed = Vec3d(300., 300., 300.)
	
	clock = pygame.time.Clock()
	
	w = SCREEN_SIZE[0]
	h = SCREEN_SIZE[1]
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
		
		screen.fill((0, 0, 0))
		
		pressed_keys = pygame.key.get_pressed()
		
		time_passed = clock.tick()
		time_passed_seconds = time_passed / 1000.
		
		direction = Vec3d(0,0,0)
		
		if pressed_keys[K_LEFT]:
			direction[0] = -1.
		elif pressed_keys[K_RIGHT]:
			direction[0] = 1.
		
		if pressed_keys[K_UP]:
			direction[1] = -1.
		elif pressed_keys[K_DOWN]:
			direction[1] = 1.
		
		if pressed_keys[K_q]:
			direction[2] = 1.
		elif pressed_keys[K_a]:
			direction[2] = -1
		
		if pressed_keys[K_w]:
			fov = min(179., fov+1.)
			viewing_distance = calculate_viewing_distance(radians(fov), w)
		elif pressed_keys[K_s]:
			fov = max(1., fov-1.)
			viewing_distance = calculate_viewing_distance(radians(fov), w)
			
		camera_position += direction * camera_speed * time_passed_seconds
		
		
		for point in points:
			x, y, z = point - camera_position
			if z < 0:
				x = x*viewing_distance/z
				y = -y*viewing_distance/z
				x += center_x
				y += center_y
				lx = x-ball_center_x
				ly = y-ball_center_y
				if lx >0 and lx<w-ball_center_x and y>0 and y < h-ball_center_y:
					screen.blit(ball, (lx, ly))
				
		
		diagram_width = w / 4.
		col = (0, 255, 0)
		diagram_points = []
		diagram_points.append( (diagram_width/2, 100 +viewing_distance/4) )
		diagram_points.append( (0, 100))
		diagram_points.append( (diagram_width, 100) )
		diagram_points.append( (diagram_width/2, 100 +viewing_distance/4) )
		diagram_points.append( (diagram_width/2, 100) )
		
		pygame.draw.lines(screen, col, False, diagram_points, 2)
		
		
		white = (0, 0, 255)
		cam_text = font.render("camera = " + str(camera_position), True, white)
		screen.blit(cam_text, (5,5))
		fov_text = font.render("field of view = %i"%int(fov), True, white)
		screen.blit(fov_text, (5,35))
		txt = "viewing distance = %.3f"%viewing_distance
		d_text = font.render(txt, True, white)
		screen.blit(d_text, (5,65))
		
		pygame.display.update()
		
		
if __name__ == "__main__":
	run()
		
		
		