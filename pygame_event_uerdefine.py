import pygame
from pygame.locals import *
from sys import exit
 
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
font = pygame.font.SysFont("arial", 16)
font_height = font.get_linesize()

print("pygame.USEREVENT = ", pygame.USEREVENT)
print("font_height = ", font_height)

#my_event = pygame.event.Event(KEYDOWN, key=K_SPACE, mod=0, unicode = u' ')
#my_event = pygame.event.Event(KEYDOEN, {"key":K_SPACE, "mod":0, "unicode":u' '})

CATONKEYBOARD = pygame.USEREVENT+1
my_event = pygame.event.Event(CATONKEYBOARD, message="Bad cat!")
pygame.event.post(my_event)

y=480-font_height
while True:
  screen.fill((255,255,255))
  for event in pygame.event.get():
    if event.type == QUIT:
      exit()
    elif event.type == CATONKEYBOARD:
      #print event.message
      screen.blit(font.render(event.message, True, (0,255,0)), (0,y))
      y -= font_height
    elif event.type == KEYDOWN:
      if event.key == K_ESCAPE:
        exit()
      elif event.key == K_SPACE:
        #pygame.event.post(my_event)
        #print("my event posted")
        screen.blit(font.render("my event posted", True, (0,255,0)), (0,y))
        y -= font_height
    else:
      screen.blit(font.render("other event posted", True, (0,255,0)), (0,y))
      y -= font_height
    if y<0:
      y=480-font_height
    #print("y=",y)
    pygame.display.update()