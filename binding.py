import pygame,os
# Key bindings for the keyboard

pygame.mixer.pre_init(44100, -16, 1, 2048)
pygame.mixer.init()

# Audio Files
gameFolder = os.path.dirname(__file__)
soundFolder = os.path.join(gameFolder,"sounds")

keybind = {}
binds = open('key_bind.config').read().split("\n")
for line in binds:
	l = line.split(" ")
	k = ord(l[0])
	v = pygame.mixer.Sound(os.path.join(soundFolder,l[1]+'.wav'))
	keybind[k] = v

print("Keys binded as per config")
