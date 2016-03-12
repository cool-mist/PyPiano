import pygame
import pygame.sndarray, numpy
from binding import *

# SETTINGS

WIDTH = 200
HEIGHT = 200
TITLE = 'You Will Be Surprized To Know'

#colors
WHITE = (0,0,0)
BLACK = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
windowSize = (WIDTH,HEIGHT)

pygame.init()

screen = pygame.display.set_mode(windowSize)


class Keyboard:
	def __init__(self):
		# Initialize
		self.screen = screen
		self.playing = False
		pygame.display.set_caption(TITLE)
		screen.fill(BLUE)

	def run(self):
		self.playing = True
		while self.playing:
			self.events()
			self.play()

	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.quit()
			if event.type == pygame.KEYDOWN:
				# Handle Key events 
				if event.key == pygame.K_SPACE:
					self.quit()
			

	def play(self):
		keys = pygame.key.get_pressed()   
		k = 0
		while k < len(keys):
			if k in keybind:
				if keys[k]:
					if not pressed[k]:
						pressed[k] = True
						keybind[k].play(loops = -1)
				else:
					pressed[k] = False
					keybind[k].stop()

			k += 1
	def quit(self):
		self.playing = False
		pygame.quit()
		quit()
pressed = {}
for i in keybind:
	pressed[i] = False
k = Keyboard()
k.run()