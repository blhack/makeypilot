#!/usr/bin/python

import pygame
import sys
import os
from pygame.locals import *

size = width, height = 600,400
screen = pygame.display.set_mode(size)

control_keys = ["up","down","left","right","forward","backward","takeoff"]
controls = {}
pygame.font.init()
font = pygame.font.Font(None, 36)

def show_text(message):
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((250,250,250))
	text = font.render(message, 1, (255,10,10))
	textpos = text.get_rect()
	textpos.centerx = background.get_rect().centerx
	background.blit(text,textpos)
	screen.blit(background, (0, 0))


index = 0
while 1:
	if index <= 6:
		show_text(control_keys[index])
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == KEYDOWN:
			print index
			if index <= 6:
				controls[event.key] = control_keys[index]
				index+=1
			else:
				try:
					show_text(controls[event.key])
				except:
					show_text("That isn't a valid key")
		else:
			show_text("")

	pygame.display.flip()
