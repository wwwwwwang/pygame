# -*- coding: utf-8 -*-
SCREEN_SIZE = (800, 600)

MUSIC_PATH = "./MUSIC"

import pygame
from pygame.locals import *
from math import sqrt
import os
import os.path
from Vector2DClass import Vec2d
from mutagen.mp3 import MP3

def get_music(path):
	raw_filenames = os.listdir(path)
	
	music_files = []
	for filename in raw_filenames:
		if filename.lower().endswith('.ogg') or filename.lower().endswith('.mp3'):
			music_files.append(os.path.join(path, filename))
	
	return sorted(music_files)

def get_time(time):
	t = int(time + 0.5)
	m = t//60
	s = t%60
	r = str("%02d:%02d"%(m,s))
	return r
	
class Button(object):
	def __init__(self, image_filename, position):
		self.position = position
		self.image = pygame.image.load(image_filename)
		self.mouse_coverd = False
		
	def render(self, surface):
		x, y = self.position
		if self.mouse_coverd == True:
			x += 10
		w, h = self.image.get_size()
		x -= w/2.
		y -= h/2.
		surface.blit(self.image, (x, y))
		
	def is_covered(self, point):
		point_x, point_y = point
		x, y = self.position
		w, h = self.image.get_size()
		x -= w/2.
		y -= h/2.
		
		in_x = point_x >= x and point_x < x+w
		in_y = point_y >= y and point_y < y+h
		return in_x and in_y
		
	
def run():
	
	pygame.mixer.pre_init(44100, 16, 2, 1024*4)
	pygame.init()
	screen = pygame.display.set_mode(SCREEN_SIZE, 0)
	pygame.display.set_caption("XiaoLI Player *_*")
	
	font = pygame.font.SysFont("simsunnsimsun", 50, False)
	
	x = 100
	y = 500
	button_width = 200
	
	buttons = {}
	buttons["prev"] = Button("prev.png", Vec2d(x, y))
	#buttons["pause"] = Button("pause.png", Vec2d(x+button_width*1, y))
	buttons["stop"] = Button("stop.png", Vec2d(x+button_width*1, y))
	buttons["play"] = Button("play.png", Vec2d(x+button_width*2, y))
	buttons["next"] = Button("next.png", Vec2d(x+button_width*3, y))
	
	music_filenames = get_music(MUSIC_PATH)
	if len(music_filenames) == 0:
		print("No music files found in ", MUSIC_PATH)
		return
	else:
		print("There are %d songs imported in %s."%(len(music_filenames), MUSIC_PATH))
	
	white = (255, 255, 255)
	label_surfaces = []
	total_length = ''
	now_length = ''
	
	
	for filename in music_filenames:
		txt = os.path.split(filename)[-1]
		#print("Track:", txt)
		txt = txt.split('.')[0]#.decode('gb2312')
		surface = font.render(txt, True, (100, 0, 100))
		label_surfaces.append(surface)
		
	current_track = 0
	max_tracks = len(music_filenames)
	pygame.mixer.music.load( music_filenames[current_track] )
	
	clock = pygame.time.Clock()
	playing = False
	paused = True
	
	TRACK_END = USEREVENT + 1
	pygame.mixer.music.set_endevent(TRACK_END)
	
	while True:
		button_pressed = None
		
		for event in  pygame.event.get():
			if event.type == QUIT:
				return
			
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					return
				elif event.key == K_LEFT:
					button_pressed = "prev"
				elif event.key == K_RIGHT:
					button_pressed = "next"
				elif event.key == K_SPACE:
					button_pressed = "play"
			
			if event.type == MOUSEBUTTONDOWN:
				#for button_name, button in buttons.iteritems():
				for button_name, button in buttons.items():
					if button.is_covered(event.pos):
						#print(button_name," is pressed!")
						button.position += 10
						button_pressed = button_name
						break
						
			if event.type == MOUSEBUTTONUP:
				#for button_name, button in buttons.iteritems():
				for button_name, button in buttons.items():
					if button.is_covered(event.pos):
						#print(button_name," is unpressed!")
						button.position -= 10
						#button_pressed = button_name
						break
						
			if event.type == TRACK_END:
				button_pressed = "next"
			
			pos = pygame.mouse.get_pos()
			for button_name, button in buttons.items():
				if button.is_covered(pos):
					#print(button_name," is covered by mouse!")
					button.mouse_coverd = True
					break
				else:
					button.mouse_coverd = False
			
			if button_pressed is not None:
				if button_pressed == "next":
					current_track = (current_track + 1)%max_tracks
					pygame.mixer.music.load( (music_filenames[current_track]) )
				
					if playing:
						pygame.mixer.music.play()
					
				elif button_pressed == "prev":
					if pygame.mixer.music.get_pos() > 3000:
						pygame.mixer.music.stop()
						pygame.mixer.music.play()
					else:
						current_track = (current_track -1) % max_tracks
						pygame.mixer.music.load( (music_filenames[current_track]) )
						
						if playing:
							pygame.mixer.music.play()
				
				#elif button_pressed == "pause":
				#	if paused:
				#		pygame.mixer.music.unpause()
				#		paused = False
				#	else:
				#		pygame.mixer.music.pause()
				#		paused = True
						
				elif button_pressed == "stop":
					pygame.mixer.music.stop()
					playing = False
					paused = True
					buttons["play"].image = pygame.image.load("play.png")
				
				elif button_pressed == "play":
					if paused and not playing:
						pygame.mixer.music.play()
						playing = True
						paused = False
						buttons["play"].image = pygame.image.load("pause.png")
					elif paused and playing:
						pygame.mixer.music.unpause()
						paused = False
						playing = True
						buttons["play"].image = pygame.image.load("pause.png")
					else:
						pygame.mixer.music.pause()
						paused = True
						#playing = False
						buttons["play"].image = pygame.image.load("play.png")
							
		
		screen.fill(white)
		
		label = label_surfaces[current_track]
		w, h = label.get_size()
		screen_w = SCREEN_SIZE[0]
		screen.blit(label, ((screen_w-w)/2,50))
		
		audio = MP3(music_filenames[current_track])
		#print(audio.info.length)
		total_length = get_time(audio.info.length)
		now_length = get_time(pygame.mixer.music.get_pos()/1000.)
		
		time_surface = font.render(now_length +'/'+total_length, True, (100, 100, 100))
		screen.blit(time_surface , ((screen_w-300)/2,100))
		
		for button in buttons.values():
			button.render(screen)
			
		clock.tick(30)
		pygame.display.update()
		
if __name__ == "__main__":
	run()
	