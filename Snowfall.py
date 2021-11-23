import pygame
import random
import sys
import time

MAX_SCREEN1 = 1366
MAX_SCREEN2 = 768
MAX_SNOW = 100
SIZE_SNOW = 80

class Snow():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(2, 5)
        self.img_num = random.randint(1, 5)
        self.image_filename = "snow" + str(self.img_num) + ".png"
        self.image = pygame.image.load(self.image_filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (SIZE_SNOW, SIZE_SNOW))


    def move_snow(self):
        self.y += self.speed
        if self.y > MAX_SCREEN2:
            self.y = 0 - SIZE_SNOW

        i = random.randint(1,3)
        if i == 1:
            self.x += 1
            if self.x > MAX_SCREEN1:
                self.x = 0 - SIZE_SNOW
        elif i == 2:
            self.x -= 1
            if self.x < (0 - SIZE_SNOW):
                self.x = MAX_SCREEN1

    def draw_snow(self):
        screen.blit(self.image, (self.x, self.y))


def initialize_snow(MAX_SNOW, snowfall):
    for i in range(0, MAX_SNOW):
        xx = random.randint(0, MAX_SCREEN1)
        yy = random.randint(0, MAX_SCREEN2)
        snowfall.append(Snow(xx, yy))

def need_exit():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            sys.exit()


pygame.init()
pygame.mixer.music.load('jinglebells.mp3') 
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
screen = pygame.display.set_mode((MAX_SCREEN1, MAX_SCREEN2), pygame.FULLSCREEN)
bg_color = (0, 0, 0)
snowfall = []

initialize_snow(MAX_SNOW, snowfall)

while True:
    screen.fill(bg_color)
    need_exit()
    for i in snowfall:
        i.move_snow()
        i.draw_snow()
    time.sleep(0.0055)
    pygame.display.flip()